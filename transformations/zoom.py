import cv2 
import random 

def zoomLabel(x, y, w , h, zoomSize, zoomCut, imgW, imgH ):
    cX = x * zoomSize[0]
    cY = y * zoomSize[1]
    W = ( w * zoomSize[0] * 0.5)
    H = ( h * zoomSize[1] * 0.5)
    top = cY - H 
    bottom = cY + H
    left = cX - W
    right = cX + W

    newMinX = zoomCut[0] if left <= zoomCut[0] else left
    newMaxX = zoomCut[1] if right >= zoomCut[1] else right
    newMinY = zoomCut[2] if top <= zoomCut[2] else top
    newMaxY = zoomCut[3] if bottom >= zoomCut[3] else bottom
    
    boxOutSideOfImage = newMinX >= zoomCut[1] or newMaxX <= zoomCut[0] or  newMinY >= zoomCut[3] or newMaxY <= zoomCut[2]
    boxNegative = (newMaxX - newMinX) <= 0 or (newMaxY - newMinY) <= 0 

    if  boxOutSideOfImage or boxNegative :
        return False, 0, 0, 0, 0

    newW = ( (newMaxX - newMinX) /imgW )
    newH = ( (newMaxY - newMinY) /imgH )
    newCX = (newMinX - zoomCut[0] ) / imgW + newW/2
    newCY = (newMinY - zoomCut[2] ) / imgH + newH/2
    
    print("prev:", x,y,w,h, "new:", newCX, newCY, newW, newH, "numeros", newMinX, newMaxX,newMinY,newMaxY)
    return True, newCX, newCY, newW, newH


def getCenterSurface(weight, height, zoomX, zoomY, axe):

    if axe == 0:
        minX = round (weight / 2)
        maxX = round (weight * (zoomX - 0.5))
        return minX,maxX
    else:
        minY = round (height / 2)
        maxY = round (height * ( zoomY - 0.5) )
        return minY, maxY


def zoomImage(image, labels = None, zoomX = 1, zoomY = 1):

    imgW, imgH = image.shape[1], image.shape[0]

    cX = round(imgW/2) if zoomX == 1 else random.randrange(*getCenterSurface(imgW, imgH, zoomX, zoomY, 0))
    cY = round(imgH/2) if zoomY == 1 else random.randrange(*getCenterSurface(imgW, imgH, zoomX, zoomY, 1))

    minX = cX - round(imgW/2)
    maxX = cX + round(imgW/2)
    minY = cY - round(imgH/2)
    maxY = cY + round(imgH/2)

    resizeW = int(imgW * zoomX)
    resizeH = int(imgH * zoomY)
    
    resized = cv2.resize(image, (resizeW, resizeH  ), interpolation = cv2.INTER_AREA)
    zoomedImage = image if (zoomX == 1 and zoomY == 1) else resized[minY:maxY, minX:maxX]

    zoomSize = [ resizeW, resizeH ]
    zoomCut = [ minX, maxX, minY, maxY ]
    
    new_labels = []
    for label in labels:
        inside, newX, newY, newW, newH = zoomLabel(label[1] , label[2],label[3] , label[4], zoomSize, zoomCut, imgW, imgH )
        
        if inside:
            new_labels.append( [label[0], newX, newY , newW, newH] )
        

    return zoomedImage, new_labels
    