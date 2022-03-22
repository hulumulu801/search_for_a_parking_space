#!/usr/bin/env python3
# -*- coding: utf:8 -*-
import cv2

class ResizeCV2:
    def __init__(self, *args):
        arg_0 = args[0]
        arg_1 = args[1]
        arg_2 = args[2]
        if isinstance(arg_0, int):
            self.width_resize_img = arg_0
        if isinstance(arg_1, int):
            self.height_resize_img = arg_1
        self.image = arg_2

    def return_resize_img(self):
        dim = (self.width_resize_img, self.height_resize_img)
        resize_img = cv2.resize(self.image, dim, interpolation=cv2.INTER_AREA)
        return resize_img

    def main(self):
        resize_img = self.return_resize_img()
        return resize_img
