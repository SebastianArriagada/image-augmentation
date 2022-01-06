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
