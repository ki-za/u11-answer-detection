import cv2 as cv
from cv2.typing import MatLike


def prepare_img_for_contouring(img: MatLike):
    img_gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY) if len(img.shape) == 3 else img
    img_blur = cv.blur(img_gray, (1, 1))
    return img_blur
