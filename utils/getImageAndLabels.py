import cv2

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

def getImageAndLabels(image, imagesPath):

    imagePath = imagesPath + image

    labels = getLabels(image, imagesPath)

    try:
        image = cv2.imread(imagePath)
    except:
        print("An error occurred while trying to load the image, url:", imagePath)

    new_labels = []
        
    for label in labels:
        try: 
            len(label) == 5
        except:
            print("check the number of columns, input", label)
            continue
        x = float(label[1])
        y = float(label[2])
        w = float(label[3])
        h = float(label[4])
        new_labels.append([label[0], x, y, w, h])
    
    return image, new_labels

