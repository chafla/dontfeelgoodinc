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

    def DesTheImage(self, level, _):
        height, width, _ = self.img.shape

        numOfSquaresWidth = 25
        numOfSquaresHeight = 25

        widthSize = int(width / numOfSquaresWidth)
        heightSize = int(height / numOfSquaresHeight)

        newImg = np.zeros((height, width, 3))

        for i in reversed(range(0, numOfSquaresWidth)):
            for j in reversed(range(0, numOfSquaresHeight)):

                if j == numOfSquaresHeight - 1 and i == numOfSquaresWidth - 1:
                    newImg[heightSize * j: (heightSize * j) + 2 * heightSize, widthSize * i: (widthSize * i) + 2 * widthSize + self.Algorithmic(level, i, numOfSquaresWidth), :] \
                        = self.img[heightSize * j: (heightSize * j) + 2 * heightSize,  widthSize * i: (widthSize * i) + 2 * widthSize].copy()

                elif j == numOfSquaresHeight - 1:
                    newImg[heightSize * j: (heightSize * j) + 2 * heightSize, widthSize * i: (widthSize * i) + widthSize + self.Algorithmic(level, i, numOfSquaresWidth), :] \
                        = self.img[heightSize * j: (heightSize * j) + 2 * heightSize,  widthSize * i: (widthSize * i) + widthSize].copy()

                elif i == numOfSquaresWidth - 1:
                    newImg[heightSize * j: (heightSize * j) + heightSize, widthSize * i: (widthSize * i) + 2 * widthSize + self.Algorithmic(level, i, numOfSquaresWidth), :] \
                        = self.img[heightSize * j: (heightSize * j) + heightSize, widthSize * i: (widthSize * i) + 2 * widthSize].copy()

                else:
                    newImg[heightSize * j: (heightSize * j) + heightSize, widthSize * i + self.Algorithmic(level, i, numOfSquaresWidth): (widthSize * i) + widthSize + self.Algorithmic(level, i, numOfSquaresWidth), :] \
                        = self.img[heightSize * j: (heightSize * j) + heightSize, widthSize * i: (widthSize * i) + widthSize].copy()


                """
                cv.imshow("image", newImg)

                cv.waitKey(0)
                cv.destroyAllWindows()
                """

                """
                if j == numOfSquaresHeight - 1 and i == numOfSquaresWidth - 1:
                    self.img[heightSize * j: (heightSize * j) + 2*heightSize,  widthSize * i: (widthSize * i) + 2*widthSize] = [69, 69, 69]
                elif j == numOfSquaresHeight - 1:
                    self.img[heightSize * j: (heightSize * j) + 2*heightSize, widthSize * i: (widthSize * i) + widthSize] = [69, 69, 69]
                elif i == numOfSquaresWidth - 1:
                    self.img[heightSize * j: (heightSize * j) + heightSize, widthSize * i: (widthSize * i) + 2*widthSize] = [69, 69, 69]
                else:
                    self.img[heightSize*j : (heightSize * j)+heightSize, widthSize*i : (widthSize*i)+widthSize] = [69, 69, 69]
                self.PrintImage()
                """

                """
                if j == numOfSquaresHeight - 1 and i == numOfSquaresWidth - 1:
                    temp =\
                        self.img[heightSize * j: (heightSize * j) + 2 * heightSize,
                        widthSize * i:
                        (widthSize * i) + 2 * widthSize]

                    self.img[heightSize * j: (heightSize * j) + 2 * heightSize,
                        widthSize * i: (widthSize * i) + 2 * widthSize]\
                        = [0,0,0]

                    self.img[heightSize * j: (heightSize * j) + 2 * heightSize,
                        widthSize * i
                        + self.Algorithmic(level,i,numOfSquaresWidth):
                        (widthSize * i) + 2 * widthSize
                        + self.Algorithmic(level,i,numOfSquaresWidth)]\
                        = temp[:,:,:]


                elif j == numOfSquaresHeight - 1:
                    temp = self.img[heightSize * j: (heightSize * j) + 2 * heightSize, widthSize * i: (widthSize * i) + widthSize]
                    self.img[heightSize * j: (heightSize * j) + 2 * heightSize, widthSize * i: (widthSize * i) + widthSize] = [0, 0, 0]
                    self.img[heightSize * j: (heightSize * j) + 2 * heightSize, widthSize * i + self.Algorithmic(level, i, numOfSquaresWidth): (widthSize * i) + widthSize
                                                                                   + self.Algorithmic(level, i,
                                                                                                      numOfSquaresWidth)] = temp
                elif i == numOfSquaresWidth - 1:
                    temp = self.img[heightSize * j: (heightSize * j) + heightSize, widthSize * i: (widthSize * i) + 2 * widthSize]
                    self.img[heightSize * j: (heightSize * j) + heightSize, widthSize * i: (widthSize * i) + 2 * widthSize] = [0, 0, 0]
                    self.img[heightSize * j: (heightSize * j) + heightSize, widthSize * i + self.Algorithmic(level, i, numOfSquaresWidth): (widthSize * i) + 2 * widthSize
                                                                                   + self.Algorithmic(level, i, numOfSquaresWidth)] = temp
                else:
                    temp = self.img[heightSize * j: (heightSize * j) + heightSize, widthSize * i: (widthSize * i) + widthSize]
                    self.img[heightSize * j: (heightSize * j) + heightSize, widthSize * i: (widthSize * i) + widthSize] = [0, 0, 0]
                    self.img[heightSize * j: (heightSize * j) + heightSize, widthSize * i + self.Algorithmic(level, i, numOfSquaresWidth): (widthSize * i) + widthSize
                                                                                   + self.Algorithmic(level, i, numOfSquaresWidth)] = temp
                """
        cv.imshow("image", newImg)

        cv.waitKey(0)


    def Algorithmic(self, level, depth, numOfSquaresWidth) -> int:
        #return int(10 * pow(10, depth/numOfSquaresWidth - level))
        return 100


