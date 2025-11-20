from typing import List, Sequence
import cv2 as cv
from cv2.typing import MatLike
from numpy._typing import _UnknownType


def find_all_in_contours(contours: Sequence[MatLike]):
    contours_poly = []
    boundRect = []
    centers = []
    radius = []
    for i, c in enumerate(contours):
        contours_poly[i] = cv.approxPolyDP(c, 3, True)
        boundRect[i] = cv.boundingRect(contours_poly[i])
        centers[i], radius[i] = cv.minEnclosingCircle(contours_poly[i])

    return contours_poly, boundRect, centers, radius


def get_rectangles_in_contours(contours: Sequence[MatLike]) -> List:
    boundingRectangles = []
    for contour in contours:
        polygons = cv.approxPolyDP(contour, 3, True)
        rectangle = cv.boundingRect(polygons)
        boundingRectangles.append(rectangle)

    return boundingRectangles


ANSWER_TO_HEIGHT_RATIO = (8.81, 8.99)
ANSWER_TO_WIDTH_RATIO = (8.70, 8.97)


def get_answer_boxes(
    img: MatLike, boundingBoxes: List[tuple[int, int, int, int]]
) -> List[tuple[int, int, int, int]]:
    imgHeight = img.shape[0]
    imgWidth = img.shape[1]
    print("image height: ", imgHeight)
    print("image width: ", imgWidth)

    validAnswerBoxes = []

    for box in boundingBoxes:
        _, _, height, width = box
        boxToHeightRatio = imgHeight / height
        boxToWidthRatio = imgWidth / width
        if (
            ANSWER_TO_HEIGHT_RATIO[0] <= boxToHeightRatio <= ANSWER_TO_HEIGHT_RATIO[1]
        ) and (ANSWER_TO_WIDTH_RATIO[0] <= boxToWidthRatio <= ANSWER_TO_WIDTH_RATIO[1]):
            print("valid bounding box: ", box)
            validAnswerBoxes.append(box)

    return validAnswerBoxes
