import cv2 as cv
import numpy as np


def display_window_for_img(cv_img: np.ndarray):
    while 1:
        cv.imshow("window", cv_img)
        key = cv.waitKey()
        if key == 27:
            break
        elif key == -1:
            continue
        else:
            print(key)
