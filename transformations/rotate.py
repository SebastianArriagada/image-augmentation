import cv2

def rotateLabel(x, y, w, h, rotateCode):

    if rotateCode == 1:
        newX = (1 - y)
        newY = x
        newW = h
        newH = w 

    elif rotateCode == 2:
        newX = (1 - x)
        newY = (1 - y) 
        newW = w 
        newH = h 
    
    elif rotateCode == 3:
        newX = y
        newY = (1 - x)
        newW = h 
        newH = w
    
    else:

        return x, y, w, h
    
    return newX, newY, newW, newH

    
def rotateImage(image, labels = None, rotateCode = 0):

    new_labels = []
        
    for label in labels:
        newX, newY, newW, newH = rotateLabel(label[1], label[2], label[3], label[4], rotateCode)
        new_labels.append( [label[0], newX, newY , newW, newH] )

    if rotateCode == 1:
        rorateImage = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
    elif rotateCode == 2:
        rorateImage = cv2.rotate(image, cv2.ROTATE_180)
    elif rotateCode == 3:
        rorateImage = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE
)
    else:
        return image, new_labels

    return rorateImage, new_labels