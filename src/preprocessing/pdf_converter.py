import cv2 as cv
import numpy as np
from pdf2image import convert_from_path

from config import INPUT_PDF_DIR


# returns a list of cv2 formatted images (BGR)
def pdf_to_cv_images(pdf_name: str, input_dir=INPUT_PDF_DIR, page_limit: int = -1):
    pdf_path = input_dir / pdf_name

    if not pdf_path.exists():
        raise FileNotFoundError(f"pdf not found at: {pdf_path}")

    # use pdf2image lib function to get img from pdf
    # return PIL img
    pil_imgs = convert_from_path(pdf_path)

    # convert RGB PIL img to CV2 compatible BGR numpy arr
    # must loop through all pages in the pdf

    # slice array if page a page limit is requested
    if page_limit != -1 and page_limit >= 0:
        pil_imgs = pil_imgs[:page_limit]

    cv_imgs = []
    for page in pil_imgs:
        cv_img = cv.cvtColor(np.array(page), cv.COLOR_RGB2BGR)
        cv_imgs.append(cv_img)

    return cv_imgs
