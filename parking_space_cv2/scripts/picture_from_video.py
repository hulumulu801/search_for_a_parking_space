#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import cv2
from scripts.resize_file import ResizeCV2
from scripts.abs_path_file import ReturnPathToFile

class PicturefromVideo:
    def __init__(self, abs_path_file_video: str, width_resize: int, height_resize: int):
        self.video_file = abs_path_file_video
        self.width_resize = width_resize
        self.height_resize = height_resize

    def video_to_frames(self, video_file, width_resize, height_resize):
        count = 0
        path = "cashe/picts"
        abs_path = ReturnPathToFile(path).main()
        video_cap = cv2.VideoCapture(video_file)

        while video_cap.isOpened():
            success, image = video_cap.read()
            if count == 1:
                break
            else:
                full_name = f"{abs_path}/{video_file.split('/')[-1].split('.')[0]}.png"

                resize_img = ResizeCV2(width_resize, height_resize, image).main() # изменение входного изображения

                cv2.imwrite(full_name, resize_img)
                count += 1
        return full_name

    def main(self):
        video_file = self.video_file
        width_resize = self.width_resize
        height_resize = self.height_resize
        return self.video_to_frames(video_file, width_resize, height_resize)
