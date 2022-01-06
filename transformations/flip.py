import cv2


def flipLabel(x, y, flipCode):

    if flipCode == 0: 
        yFlipped  = (1 - y) 
        return x, yFlipped
    
    elif flipCode == 1:
        xFlipped = (1 - x)
        return xFlipped, y
    
    elif flipCode == -1: 
        yFlipped  = (1 - y) 
        xFlipped = (1 - x)
        return xFlipped, yFlipped
    
    else:
        return x,y


def flipImage(image, labels = None, flipCode = 2):

    new_labels = []
    for label in labels:
        newX, newY = flipLabel(label[1] , label[2], flipCode)
        new_labels.append( [label[0], newX, newY , label[3], label[4]] )
        
    if flipCode in [-1,0,1]:
        flipedImage = cv2.flip(image, flipCode)

        return flipedImage, new_labels
    else:
        return image, new_labels