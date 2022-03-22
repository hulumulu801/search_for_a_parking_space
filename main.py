#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import argparse
from scripts.parking_lot_mark import ImgCV2
from scripts.parking_space_video import VideoCV2
from scripts.abs_path_file import ReturnPathToFile
from scripts.picture_from_video import PicturefromVideo

def main():
    ap = argparse.ArgumentParser(
                    prog="python3 main.py",
                    usage="%(prog)s --file VIDEO_example/1.mp4 --width_zone 25 --height_zone 75 --width_resize 1200 --height_resize 800"
    )
    ap.add_argument(
                    "--file",
                    type=str,
                    default="VIDEO_example/1.mp4",
                    metavar="",
                    help="Видео файл. По умолчанию: VIDEO_example/1.mp4"
    )
    ap.add_argument(
                    "--width_zone",
                    type=int,
                    default=25,
                    metavar="",
                    help="Ширина прямоугольника парковочного места. По умолчанию: 25"
    )
    ap.add_argument(
                    "--height_zone",
                    type=int,
                    default=75,
                    metavar="",
                    help="Длина прямоугольника парковочного места. По умолчанию: 75"
    )
    ap.add_argument(
                    "--width_resize",
                    type=int,
                    default=1200,
                    metavar="",
                    help="Ширина видео кадра. По умолчанию: 1200"
    )
    ap.add_argument(
                    "--height_resize",
                    type=int,
                    default=800,
                    metavar="",
                    help="Длина видео кадра. По умолчанию: 800"
    )

    args = vars(ap.parse_args())

    input_file_video = args["file"]

    width_zone = args['width_zone']
    height_zone = args['height_zone']

    width_resize = args['width_resize']
    height_resize = args['height_resize']

    abs_path_file_video = ReturnPathToFile(input_file_video).main() # абсолютный путь видео файла
    abs_path_file_pict = PicturefromVideo(abs_path_file_video, width_resize, height_resize).main() # абсолютный путь кроп. изображения

    question = input("Разметить парковочные места? Y/N\n")

    if str.upper(question) == "Y":
        ImgCV2(abs_path_file_pict, width_zone, height_zone).main()
    elif str.upper(question) == "N":
        abs_path_file_pickle = ImgCV2(abs_path_file_pict, width_zone, height_zone, pickle_path=True).main()
        VideoCV2(abs_path_file_pickle, abs_path_file_video, width_resize, height_resize).main()
    else:
        print("Только: Y/N\nВыход!")
        sys.exit()

if __name__ == "__main__":
    main()
