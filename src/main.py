from preprocessing.pdf import pdf_to_cv_images
from preprocessing.image import prepare_img_for_contouring
from detection.boxes import get_rectangles_in_contours
from utils.show_window import display_window_for_img
from detection.boxes import get_answer_boxes
import cv2 as cv
import random as rng

if __name__ == "__main__":
    try:
        imgs = pdf_to_cv_images("KGT-K2.pdf", page_limit=1)
        img = imgs[0]

        preparedImage = prepare_img_for_contouring(img)

        # THRESH_BINARY_INV = makes dark pixels white, and light pixels black
        _, threshhold = cv.threshold(preparedImage, 127, 255, cv.THRESH_BINARY_INV)

        # findcontours: returns
        # `contours`: list of boundary points for each shape
        # `hierarchy`: parent-child relationships between colours
        # `RETR_EXTERNAL`: retrieve external contours only, the outermost boundaries
        # `CHAIN_APPROX_SIMPLE`: compress contour points, keep only corner points
        contours, contourImage = cv.findContours(
            threshhold, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE
        )

        # get the bounding rectangles from the contours
        boundingBoxes = get_rectangles_in_contours(contours)
        answerBoxes = get_answer_boxes(img, boundingBoxes)

        # TODO: remove debug
        # print("image shape:", img.shape)
        # count = 0
        # for box in answerBoxes:
        #     print("Box Number: ", count)
        #     print("Box Data: ", box)
        #     count += 1

        # draw the rectanges
        for (
            x,
            y,
            width,
            height,
        ) in answerBoxes:
            color = (rng.randint(0, 256), rng.randint(0, 256), rng.randint(0, 256))

            cv.rectangle(
                img, (int(x), int(y)), (int(x + width), int(y + height)), color, 2
            )

        # contour_annotated_img = cv.drawContours(img, contours, -1, (0, 255, 0), 3)

        # print("contours length: ", len(contours))
        # print("contours example 1: ", contours[1])

        # largest_contour = max(contours, key=cv.contourArea)

        # get the bounding rectangle
        # `x` and `y` are top left coordinates
        # x, y, width, height = cv.boundingRect((largest_contour))

        # annotated_img = cv.rectangle(
        #     img, (x, y), (x + width, y + height), (0, 200, 100), 2
        # )
        #
        display_window_for_img(img)

    except Exception as e:
        print("Unexpected Error: ", e)
