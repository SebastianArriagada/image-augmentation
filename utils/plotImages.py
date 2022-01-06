import matplotlib.pyplot as plt
import cv2

def plotImages(imagesList, titleList, col = None, row = None):
    if (col or row) == None:
        col = 1
        row = len(imagesList)
    fig = plt.figure(figsize=(row*2,col*10))

    try:
        row > 0
    except:
        print("Is necesary at less one image")
        return False

    for i, (image, title) in enumerate(zip(imagesList, titleList)):
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        fig.add_subplot(row, col, i + 1)
        plt.imshow(image)
        plt.axis('off')
        plt.title(title)
    plt.show()
