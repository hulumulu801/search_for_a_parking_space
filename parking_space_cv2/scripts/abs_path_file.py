#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

class ReturnPathToFile:
    def __init__(self, *args):
        arg = args[0]
        if isinstance(arg, str):
            self.file = arg

    def return_abs_path_file(self, file):
        abs_path = f"{os.path.abspath('./')}/{file}"
        if not os.path.exists(abs_path):
            os.makedirs(abs_path)
            return abs_path
        else:
            return abs_path

    def main(self):
        file = self.file
        return self.return_abs_path_file(file)
