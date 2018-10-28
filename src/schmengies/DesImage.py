import numpy as np
import cv2 as cv
import math

class DesImage(object):

    def __init__(self, filename, widthSquares=None, heightSquares=None):
        self.img = cv.imread(filename)
        self.numOfSquareHeight, self.numOfSquareWidth, _ = self.img.shape
        if widthSquares is not None:
            self.numOfSquareWidth = widthSquares
        if heightSquares is not None:
            self.numOfSquareHeight = heightSquares

    def ReturnImage(self):
        return self.img


    def PrintImage(self):
        cv.imshow("*S N A P*", self.img)
        cv.waitKey(0)
        cv.destroyAllWindows()

    def DesTheImage(self, level, override=False):
        height, width, _ = self.img.shape

        numOfSquaresWidth = self.numOfSquareWidth
        numOfSquaresHeight = self.numOfSquareHeight

        widthSize = int(width / numOfSquaresWidth)
        heightSize = int(height / numOfSquaresHeight)

        newImg = np.zeros((height, width, 3), dtype=np.uint8)

        down = True

        for i in reversed(range(0, numOfSquaresWidth)):
            for j in reversed(range(0, numOfSquaresHeight)):


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


                if down:
                    try:
                        if j == numOfSquaresHeight - 1 and i == numOfSquaresWidth - 1:
                            newImg[heightSize * j + level*self.Algorithmic(level, i, numOfSquaresWidth): (heightSize * j) + 2 * heightSize + level*self.Algorithmic(level, i, numOfSquaresWidth),
                            widthSize * i: (widthSize * i) + 2 * widthSize + self.Algorithmic(level, i, numOfSquaresWidth), :] \
                                = self.img[heightSize * j: (heightSize * j) + 2 * heightSize,
                                  widthSize * i: (widthSize * i) + 2 * widthSize].copy()

                        elif j == numOfSquaresHeight - 1:
                            newImg[heightSize * j + level*self.Algorithmic(level, i, numOfSquaresWidth): (heightSize * j) + 2 * heightSize + level*self.Algorithmic(level, i, numOfSquaresWidth),
                            widthSize * i + self.Algorithmic(level, i, numOfSquaresWidth): (widthSize * i) + widthSize + self.Algorithmic(level, i, numOfSquaresWidth), :] \
                                = self.img[heightSize * j: (heightSize * j) + 2 * heightSize,
                                  widthSize * i: (widthSize * i) + widthSize].copy()

                        elif i == numOfSquaresWidth - 1:
                            newImg[heightSize * j + level*self.Algorithmic(level, i, numOfSquaresWidth): (heightSize * j) + heightSize + level*self.Algorithmic(level, i, numOfSquaresWidth),
                            widthSize * i: (widthSize * i) + 2 * widthSize + self.Algorithmic(level, i, numOfSquaresWidth), :] \
                                = self.img[heightSize * j: (heightSize * j) + heightSize,
                                  widthSize * i: (widthSize * i) + 2 * widthSize].copy()

                        else:
                            newImg[heightSize * j + level*self.Algorithmic(level, i, numOfSquaresWidth): (heightSize * j) + heightSize + level*self.Algorithmic(level, i, numOfSquaresWidth),
                            widthSize * i + self.Algorithmic(level, i, numOfSquaresWidth): (widthSize * i) + widthSize + self.Algorithmic(level, i, numOfSquaresWidth), :] \
                                = self.img[heightSize * j: (heightSize * j) + heightSize,
                                  widthSize * i: (widthSize * i) + widthSize].copy()
                    except ValueError as e:
                        print("\N{OK HAND SIGN}", e)
                        newImg[heightSize * j: (heightSize * j) + heightSize,
                        widthSize * i: ( widthSize * i) + widthSize] = self.img[heightSize * j: (heightSize * j) + heightSize,
                            widthSize * i: (widthSize * i) + widthSize].copy()
                    down = False

                else:
                    try:
                        if j == numOfSquaresHeight - 1 and i == numOfSquaresWidth - 1:
                            newImg[heightSize * j - level*self.Algorithmic(level, i, numOfSquaresWidth): (heightSize * j) + 2 * heightSize - level*self.Algorithmic(
                                level, i, numOfSquaresWidth),
                            widthSize * i: (widthSize * i) + 2 * widthSize + self.Algorithmic(level, i,
                                                                                              numOfSquaresWidth), :] \
                                = self.img[heightSize * j: (heightSize * j) + 2 * heightSize,
                                  widthSize * i: (widthSize * i) + 2 * widthSize].copy()

                        elif j == numOfSquaresHeight - 1:
                            newImg[heightSize * j - level*self.Algorithmic(level, i, numOfSquaresWidth): (heightSize * j) + 2 * heightSize - level*self.Algorithmic(
                                level, i, numOfSquaresWidth),
                            widthSize * i + self.Algorithmic(level, i, numOfSquaresWidth): (widthSize * i) + widthSize + self.Algorithmic(
                                level, i, numOfSquaresWidth), :] \
                                = self.img[heightSize * j: (heightSize * j) + 2 * heightSize,
                                  widthSize * i: (widthSize * i) + widthSize].copy()

                        elif i == numOfSquaresWidth - 1:
                            newImg[heightSize * j - level*self.Algorithmic(level, i, numOfSquaresWidth): (heightSize * j) + heightSize - level*self.Algorithmic(
                                level, i, numOfSquaresWidth),
                            widthSize * i: (widthSize * i) + 2 * widthSize + self.Algorithmic(level, i,
                                                                                              numOfSquaresWidth), :] \
                                = self.img[heightSize * j: (heightSize * j) + heightSize,
                                  widthSize * i: (widthSize * i) + 2 * widthSize].copy()

                        else:
                            newImg[heightSize * j - level*self.Algorithmic(level, i, numOfSquaresWidth): (heightSize * j) + heightSize - level*self.Algorithmic(
                                level, i, numOfSquaresWidth),
                            widthSize * i + self.Algorithmic(level, i, numOfSquaresWidth): (
                                                                                                       widthSize * i) + widthSize + self.Algorithmic(
                                level, i, numOfSquaresWidth), :] \
                                = self.img[heightSize * j: (heightSize * j) + heightSize,
                                  widthSize * i: (widthSize * i) + widthSize].copy()
                    except ValueError as e:
                        print("\N{OK HAND SIGN} ", e)
                        newImg[heightSize * j: (heightSize * j) + heightSize,
                        widthSize * i: (widthSize * i) + widthSize] = self.img[
                                                                      heightSize * j: (heightSize * j) + heightSize,
                                                                      widthSize * i: (widthSize * i) + widthSize].copy()
                    down = True

                """
                cv.imshow("image", newImg)

                cv.waitKey(0)
                cv.destroyAllWindows()
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
                """



                #roi = self.img[j * heightSize: j * heightSize + heightSize, i*widthSize:i*widthSize+widthSize]
                #newImg[j * heightSize: j * heightSize + heightSize, i*widthSize:i*widthSize+widthSize] = roi
               # roi0 = self.img[000:400,000:400,0]
                #roi1 = self.img[000:400,000:400,1]
                #roi2 = self.img[000:400,000:400,2]
                #newImg[000:400, 000:400, 0] = self.img[000:400,000:400,0]
                #newImg[000:400, 000:400, 1] = self.img[000:400,000:400,1]
                #newImg[000:400, 000:400, 2] = self.img[000:400,000:400,2]


                #cv.imshow('new img', newImg)
                #cv.waitKey(0)
                #cv.destroyAllWindows()


        #cv.imshow('new img', newImg)
        #cv.waitKey(0)
        #cv.destroyAllWindows()
        if override:
            self.img = newImg
        return newImg





    def Algorithmic(self, level, depth, numOfSquaresWidth) -> int:
        answer = int(15*pow(10, depth/numOfSquaresWidth - level/10) - 1)
        return answer


