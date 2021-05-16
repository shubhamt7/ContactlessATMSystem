import cv2
import numpy as np
from colors import black
import time

class CameraUtility:
    cameraInstance = None
    @staticmethod
    def getInstance():
        if CameraUtility.cameraInstance == None:
            CameraUtility()
        return CameraUtility.cameraInstance

    def __init__(self):
        if CameraUtility.cameraInstance !=None :
            raise Exception("This is a singleton class")
        else :
            CameraUtility.cameraInstance = cv2.VideoCapture(0)


class Fade:
    @staticmethod
    def fade(img1,img2):  # pass images here to fade between
        # while True:
        h = img1.shape[0]
        w = img1.shape[1]
        for IN in range(0, 20):
            fadein = IN / 10.0
            dst = cv2.addWeighted(img1, 1 - fadein, img2, fadein, 0)  # linear $
            cv2.imshow('Contactless ATM System', dst)
            cv2.waitKey(1)
            time.sleep(0.01)
        return  # exit function
    @staticmethod
    def fadeIn(img1):
        h = img1.shape[0]
        w = img1.shape[1]
        img2 = np.array([[black for x in range(w)] for y in range(h)], dtype="uint8")
        Fade.fade(img2,img1)
        return

    @staticmethod
    def fadeOut(img1):
        h = img1.shape[0]
        w = img1.shape[1]
        img2 = np.array([[black for x in range(w)] for y in range(h)], dtype="uint8")
        Fade.fade(img1, img2)
        return

