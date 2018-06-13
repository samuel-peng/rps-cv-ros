# rpsimgproc.py
# Source: https://github.com/samuel-peng/rps-cv-mozi
#
# MIT License
#
# Copyright (c) 2018 Samuel Joel Peng <samuelpeng1@gmail.com>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.



import time

import cv2
import numpy as np
import rpsimgproc as imp

import timer
import filters
import imutils

from colorBalance import colorBalance

class Camera():

    def __init__(self, size=10, frameRate=40, hflip=False, vflip=False):
        self.active = False
        try:
            if type(size) is not int:
                raise TypeError("Size must be an integer")
            elif 1 <= size and size <= 51:
                self.size = size
                self.hRes = size * 64
                self.vRes = size * 48
            else:
                raise ValueError("Size must be in range 1 to 51")
        except  TypeError or ValueError:
            raise
        self.cam = cv2.VideoCapture(1)
        self.cam.set(3, size * 48) #width
        self.cam.set(4, size * 64) #height

    def close(self):
        #self.stop()
        self.cam.release()

    def rotatedImage(self, image, angle):
        image_center = tuple(np.array(image.shape[1::-1]) / 2)
        #rows, cols = image.shape
        rot_mat = cv2.getRotationMatrix2D(image_center, angle, 1.0)
        result = cv2.warpAffine(image, rot_mat, image.shape[1::-1], flags=cv2.INTER_LINEAR)
        #result = cv2.warpAffine(image, rot_mat,(cols, rows))
        return result

    def processImg(self, image):
       #return imutils.rotate_bound(colorBalance(image), 270)
       #return imp.fastRotate(colorBalance(image)) #with rotation
        return colorBalance(image)

    def getOpenCVImage(self):
        if self.cam.isOpened():
            rval, frame = self.cam.read()
        #return self.processImg(frame)
        return frame

    def startPreview(self):
        cv2.namedWindow("Preview")
        if self.cam.isOpened():
            rval, frame = self.cam.read()
        else:
            rval = false
        while rval:
            #cv2.imshow("Preview", self.rotatedImage(frame, 90))
            self.processedImg = self.processImg(frame)
            cv2.imshow("Preview", self.processedImg)
            rrval, frame = self.cam.read()
            key = cv2.waitKey(20)
            if key == 27:
                break
        cv2.destroyWindow("Preview")

if __name__=="__main__":
    c = Camera(10, 40, False, False)
    c.startPreview()
