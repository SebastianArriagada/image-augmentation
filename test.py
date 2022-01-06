import numpy as np
from transformations.flip import flipImage
from os import listdir
from utils.drawBoxes import drawBoxes
from utils.getLabels import getLabels
from utils.plotImages import plotImages

def flipTest(imagesList , imagesPath):
    for image in imagesList:
        labels = getLabels(image, imagesPath)
        
        img1 = drawBoxes(*flipImage(imagesPath + image, labels, 1))
        img2 = drawBoxes(*flipImage(imagesPath + image, labels, 0))
        img3 = drawBoxes(*flipImage(imagesPath + image, labels, -1))
        imgT = drawBoxes(*flipImage(imagesPath + image, labels, 2))

        plotList = [imgT, img1, img2, img3]
        titleList = ['Ground True', 'Horizomtal flip', 'Vertical flip',  'Both flip']

        plotImages(plotList, titleList)


imagesPath = "./test-images/"
imagesList = [f for f in listdir(imagesPath) if (f.endswith('.png') or f.endswith('.jpg')) ]
