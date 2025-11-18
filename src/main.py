from preprocessing.pdf_converter import pdf_to_cv_images
from utils.show_window import display_window_for_img
import cv2 as cv

if __name__ == "__main__":
    try:
        imgs = pdf_to_cv_images("KGT-K2.pdf", page_limit=1)
        img = imgs[0]

        gray_img = cv.cvtColor(img, cv.COLOR_RGB2GRAY) if len(img.shape) == 3 else img

        # THRESH_BINARY_INV = makes dark pixels white, and light pixels black
        _, threshhold = cv.threshold(gray_img, 127, 255, cv.THRESH_BINARY_INV)

        # findcontours: returns
        # `contours`: list of boundary points for each shape
        # `hierarchy`: parent-child relationships between colours
        # `RETR_EXTERNAL`: retrieve external contours only, the outermost boundaries
        # `CHAIN_APPROX_SIMPLE`: compress contour points, keep only corner points
        contours, contour_image = cv.findContours(
            threshhold, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE
        )

        contour_annotated_img = cv.drawContours(img, contours, -1, (0, 255, 0), 3)
        # now we find the largest contour by area
        largest_contour = max(contours, key=cv.contourArea)

        # get the bounding rectangle
        # `x` and `y` are top left coordinates
        x, y, width, height = cv.boundingRect((largest_contour))

        annotated_img = cv.rectangle(
            img, (x, y), (x + width, y + height), (0, 200, 100), 2
        )

        display_window_for_img(contour_annotated_img)

    except Exception as e:
        print("Unexpected Error: ", e)
