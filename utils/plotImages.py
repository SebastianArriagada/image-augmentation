import matplotlib.pyplot as plt

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
