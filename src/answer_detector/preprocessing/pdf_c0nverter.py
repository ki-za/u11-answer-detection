import cv2 as cv
import numpy as np
from pdf2image import convert_from_path


# returns a list of cv2 formatted images (BGR)
def pdf2CvImages(pdf_path):
    pil_imgs = convert_from_path(pdf_path)
    cv_imgs = []
    for page in pil_imgs:
        cv_img = cv.cvtColor(np.array(page), cv.COLOR_RGB2BGR)
        cv_imgs.append(cv_img)
    return cv_imgs
