import numpy as np
from transformations.flip import flipImage
from utils.drawBoxes  import drawBoxes
from os import listdir
import matplotlib.pyplot as plt

def getLabels(imageName, path = './'):

    if imageName.endswith('.png'):
        txt = imageName.replace('.png','.txt')

    elif imageName.endswith('.jpg'):
        txt = imageName.replace('.jpg','.txt')

    try:
        with open(path + txt) as textFile:
            labels = [line.split() for line in textFile]
        return labels
    except:
        print("Labels not found, file:", txt)

def plotImages(imagesList, titleList):
    col = 1
    row = len(imagesList)
    fig = plt.figure(figsize=(5,10))

    try:
        row > 0
    except:
        print("Is necesary at less one image")
        return False

    for i, (image, title) in enumerate(zip(imagesList, titleList)):
        fig.add_subplot(row, col, i + 1)
        plt.imshow(image)
        plt.axis('off')
        plt.title(title)
    plt.show()

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
