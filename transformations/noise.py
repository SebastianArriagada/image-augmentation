import numpy as np
import random
import matplotlib.pyplot as plt
import cv2

def noiseImage(image, percent = 0.1, size=(1,1), noiseColor = [0,0,0]):
    imageT = image.copy()
    xImageSize, yImageSize, _ = imageT.shape
    xNoiseSize, yNoiseSize = size
    imageArea = xImageSize * yImageSize
    noiseApplied = 0
    while noiseApplied < (percent*imageArea):
        x = random.randrange(0, xImageSize - xNoiseSize)
        y = random.randrange(0, yImageSize - yNoiseSize)
        imageT[ x : x+xNoiseSize, y : y+yNoiseSize] = noiseColor
        noiseApplied += xNoiseSize * yNoiseSize
        
    return imageT
