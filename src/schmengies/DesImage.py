import numpy as np
import cv2 as cv
import math

class DesImage(object):

    def __init__(self, arg1):
        self.img = cv.imread(arg1)

    def PrintImage(self):
        cv.imshow("image", self.img)
        cv.waitKey(0)
        cv.destroyAllWindows()

    def DesTheImage(self, level, squareScale):
        height, width, _ = self.img.shape

        numOfSquaresWidth = 25
        numOfSquaresHeight = 25

        widthSize = int(width / numOfSquaresWidth)
        heightSize = int(height / numOfSquaresHeight)



        for i in reversed(range(0, numOfSquaresWidth)):
            for j in reversed(range(0, numOfSquaresHeight)):
                self.img[heightSize*j : (heightSize * j)+heightSize, widthSize*i : (widthSize*i)+widthSize] = [69, 69, 69]
                self.PrintImage()
