import cv2
import numpy as np
from matplotlib import pyplot as plt
import random

def printImage(image):
    cv2.imshow('image',image)
    cv2.waitKey()
    cv2.destroyAllWindows()

def generateRadomColor():
    b = random.randint(0, 255)
    g = random.randint(0, 255)
    r = random.randint(0, 255)
    return (b, g, r)

def translate(image, x, y):
    M = np.float32([[1, 0, x], [0, 1, y]]) # matriz de transformação
    shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
    return shifted

def rotate(image, angle, center = None, scale = 1.0):
    (h, w) = image.shape[:2]

    if center is None:
        center = (w // 2, h // 2)

    M = cv2.getRotationMatrix2D(center, angle, scale)
    rotated = cv2.warpAffine(image, M, (w, h))
    
    return rotated