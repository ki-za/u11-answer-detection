from typing import List
import cv2 as cv
from cv2.typing import MatLike

ANSWER_AREA_RATIO_WIDTH = (8.82641, 8.99615)
ANSWER_AREA_RATIO_HEIGHT = (8.71351, 8.95555)


def find_answer_areas(
    img: MatLike, boundingBoxes: List[tuple[int, int, int, int]]
) -> List[tuple[int, int, int, int]]:
    imgHeight = img.shape[0]
    imgWidth = img.shape[1]

    for box in boundingBoxes:
        _, _, height, width = box
        boxHeightRatio = imgHeight / height
        boxWidthRatio = imgWidth / width
        if not (
            ANSWER_AREA_RATIO_HEIGHT[0] <= boxHeightRatio <= ANSWER_AREA_RATIO_HEIGHT[1]
            and ANSWER_AREA_RATIO_WIDTH[0]
            <= boxWidthRatio
            <= ANSWER_AREA_RATIO_WIDTH[1]
        ):
            boundingBoxes.remove(box)

    return boundingBoxes
