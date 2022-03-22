#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import cv2
import pickle
import cvzone
import numpy as np
from scripts.resize_file import ResizeCV2

class VideoCV2:
    def __init__(
                    self,
                    abs_path_file_pickle: str,
                    abs_path_file_video: str,
                    width_resize: int,
                    height_resize: int,
                    vizual_n = False
    ):
        if isinstance(abs_path_file_pickle, str):
            self.file_pickle = abs_path_file_pickle
        if isinstance(abs_path_file_video, str):
            self.file_video = abs_path_file_video
        if isinstance(width_resize, int):
            self.width_resize = width_resize
        if isinstance(height_resize, int):
            self.height_resize = height_resize
        self.vizual_n = vizual_n

    def image_preparation(self, video_cap):
        # подготавливаем изображения
        if video_cap.get(cv2.CAP_PROP_POS_FRAMES) == video_cap.get(cv2.CAP_PROP_FRAME_COUNT):
            video_cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        success, img = video_cap.read()

        resize_img = ResizeCV2(self.width_resize, self.height_resize, img).main()

        img_gray = cv2.cvtColor(resize_img, cv2.COLOR_BGR2GRAY)
        img_blur = cv2.GaussianBlur(img_gray, (3, 3), 1)
        img_threshold = cv2.adaptiveThreshold(
                                                img_blur, 255,
                                                cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                                cv2.THRESH_BINARY_INV,
                                                25, 16
        )
        img_median = cv2.medianBlur(img_threshold, 5)
        kernel = np.ones((3, 3), np.int8)
        img_dilate = cv2.dilate(img_median, kernel, iterations=1)
        return resize_img, img_dilate

    def check_parking_space(self, pos_list, img_dilate, resize_img):
        space_count = 0
        for pos in pos_list:
            x, y = pos[0], pos[1]
            width_zone, height_zone = pos[2], pos[3]
            pos = x, y
            img_crop = img_dilate[y : y + height_zone, x : x + width_zone]
            count = cv2.countNonZero(img_crop)

            if self.vizual_n == True:
                cvzone.putTextRect(
                                    resize_img,
                                    str(count),
                                    (x, y + self.height_zone -10),
                                    scale=1,
                                    thickness=1,
                                    offset=0

                )

            if count < 300:
                color = (0, 255, 0)
                thickness = 2
                space_count += 1
            else:
                color = (0, 0, 255)
                thickness = 2
            cv2.rectangle(
                            resize_img,
                            pos,
                            (pos[0] + width_zone, pos[1] + height_zone),
                            color,
                            thickness
            )
            cvzone.putTextRect(
                                resize_img,
                                f"Free: {space_count}/{len(pos_list)}",
                                (15, 50),
                                scale=2,
                                thickness=3,
                                offset=15,
                                colorR=(0, 200, 0)
            )

    def main(self):
        video_cap = cv2.VideoCapture(self.file_video)

        with open(self.file_pickle, "rb") as f:
            pos_list = pickle.load(f)

        while True:
            resize_img, img_dilate = self.image_preparation(video_cap)
            self.check_parking_space(pos_list, img_dilate, resize_img)
            cv2.imshow("image", resize_img)
            if cv2.waitKey(100) & 0xFF == ord("q"):
                break
