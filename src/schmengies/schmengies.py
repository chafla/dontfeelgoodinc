import sys
import io
import numpy as np
import cv2 as cv
import argparse
import os.path
from src.schmengies.DesImage import DesImage


def main():
    filename = sys.argv[1]
    if os.path.isfile(filename):
        img = DesImage(filename, 25, 25)
        cv.imshow("SNAP", img.DesTheImage(14))
        cv.waitKey(0)
        cv.destroyAllWindows()
    else:
        print("FILE ", filename, " DOESNT EXIST")


if __name__ == '__main__':
    main()

