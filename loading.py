from cv2 import cv2 as cv2
import numpy as np
import os
import sys
NUM_CATEGORIES = 43

def main():
    images = load_images(sys.argv[1])
    print(images)

def load_images(folder):
    images = []

    for i in range(NUM_CATEGORIES):
        path = os.path.join(folder, i)
        filesname = 
        for filename in os.listdir(folder):
            img = cv2.imread(os.path.join(folder, filename))
            print(type(img))
            if img is not None:
                images.append(img)
        return images


if __name__ == "__main__":
    main()