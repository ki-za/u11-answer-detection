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


def find_rectangles_in_contours(contours: Sequence[MatLike]) -> List:
    boundingRectangles = []
    for contour in contours:
        polygons = cv.approxPolyDP(contour, 3, True)
        rectangle = cv.boundingRect(polygons)
        boundingRectangles.append(rectangle)

    return boundingRectangles
