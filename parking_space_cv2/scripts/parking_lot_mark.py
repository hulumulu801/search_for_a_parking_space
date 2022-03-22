#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import cv2
import pickle
from scripts.abs_path_file import ReturnPathToFile

class ImgCV2:
    def __init__(self, abs_path_file_pict: str, width_zone: int, height_zone: int, pickle_path=False):
        self.pickle_path = pickle_path
        if isinstance(abs_path_file_pict, str):
            self.abs_path_img = abs_path_file_pict
        if isinstance(width_zone, int):
            self.width_zone = width_zone
        if isinstance(height_zone, int):
            self.height_zone = height_zone
        try:
            abs_path_pickle = self.return_and_create_path_pickle()
            with open(abs_path_pickle, "rb") as f:
                self.pos_list = pickle.load(f)
        except:
            self.pos_list = []

    def return_and_create_path_pickle(self):
        aps_path_folder = ReturnPathToFile("cashe/pickle").main()
        return f"{aps_path_folder}/pickle_{self.abs_path_img.split('/')[-1].split('.')[0]}.pickle"

    def mouse_click(self, events, x, y, flags, params):
        if events == cv2.EVENT_LBUTTONDOWN:
            self.pos_list.append((x, y, self.width_zone, self.height_zone))

        if events == cv2.EVENT_RBUTTONDOWN:
            for i, pos in enumerate(self.pos_list):
                x_1, y_1 = pos[0], pos[1]
                width_zone, height_zone = pos[2], pos[3]
                if x_1 < x < x_1 + width_zone and y_1 < y < y_1 + height_zone:
                    self.pos_list.pop(i)

        abs_path_pickle = self.return_and_create_path_pickle()
        with open(abs_path_pickle, "wb") as f:
            pickle.dump(self.pos_list, f)

    def main(self):
        if self.pickle_path == True:
            return self.return_and_create_path_pickle()
        else:
            while True:
                img = cv2.imread(self.abs_path_img)
                for pos in self.pos_list:
                    w_zone, h_zone = pos[2], pos[3]
                    pos = pos[0], pos[1]
                    cv2.rectangle(img, pos, (pos[0] + w_zone, pos[1] + h_zone), (255, 0, 255), 2)

                cv2.imshow("image", img)
                cv2.setMouseCallback("image", self.mouse_click)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
