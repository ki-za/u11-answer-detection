import cv2 as cv
import numpy as np
from pdf2image import convert_from_path

from config import INPUT_PDF_DIR


def get_full_pdf_location(pdf_name: str, input_dir):
    pdf_path = input_dir / pdf_name

    if not pdf_path.exists():
        raise FileNotFoundError(f"pdf not found at: {pdf_path}")
    return pdf_path


# returns a list of cv2 formatted images (BGR)
def pdf_to_cv_images(pdf_name: str, input_dir=INPUT_PDF_DIR, page_limit: int = -1):
    # use pdf2image lib function to get img from pdf
    # return PIL img
    pil_imgs = convert_from_path(get_full_pdf_location(pdf_name, input_dir))

    # slice array if page a page limit is requested
    if page_limit != -1 and page_limit >= 0:
        pil_imgs = pil_imgs[:page_limit]

    cv_imgs = []
    for page in pil_imgs:
        cv_img = cv.cvtColor(np.array(page), cv.COLOR_RGB2BGR)
        cv_imgs.append(cv_img)

    return cv_imgs
