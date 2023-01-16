import cv2
import numpy as np
from PIL import Image


def mse(img1, img2):
    h, w = img1.shape
    print(img1.shape[0], img1.shape[1], img2.shape[0], img2.shape[1])
    diff = cv2.subtract(img1, img2)
    # err = np.sum(diff ** 2)
    # mse = err / (float(h * w))
    # return mse
    return diff


def display():
    img1 = cv2.imread("./ui_testing/shot 1668188266.0341837.bmp")
    img2 = cv2.imread("./ui_testing/shot 1668188267.5604727.bmp")

    diff = mse(img1, img2)
    assert diff is not None


def main():
    # img1 = cv2.imread('./ui_testing/shot 1668188266.0341837.bmp')
    # img2 = cv2.imread('./ui_testing/shot 1668188267.5604727.bmp')
    img1 = Image.open("ui_testing/shot 1668188266.0341837.bmp")
    img2 = Image.open("ui_testing/shot 1668188267.5604727.bmp")
    pixel_checkList = [[85, 244], [148, 41], [136, 421]]
    img1_np = np.array(img1, dtype=np.uint8)
    img2_np = np.array(img2, dtype=np.uint8)
    for position in pixel_checkList:
        if np.array_equal(img1_np, img2_np):
            print(f"for coordinates: {position}, equal")
        else:
            print(f"for coordinates: {position}, not Equal")


if __name__ == "__main__":
    main()
