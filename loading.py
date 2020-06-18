from cv2 import cv2 as cv2
import numpy as np
import os
import sys
EPOCHS = 10
IMG_WIDTH = 30
IMG_HEIGHT = 30
NUM_CATEGORIES = 43
TEST_SIZE = 0.4


def main():
    images = load_images(sys.argv[1])
    # print(images)

def load_images(folder):
    images = []
    for i in range(NUM_CATEGORIES):
        path = os.path.join(folder, str(i))
        for filename in os.listdir(path):
            full = os.path.join(folder, str(i), filename)
            img = cv2.imread(full)
            img_resize = cv2.resize(img, (IMG_WIDTH, IMG_HEIGHT))
            print(img_resize.shape)
            images.append(img_resize)
    return images

if __name__ == "__main__":
    main()
