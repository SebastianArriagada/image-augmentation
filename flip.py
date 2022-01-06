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


def flipImage(url, labels = None, flipCode = 2):
    try:
        image = cv2.imread(url)
    except:
        print("An error occurred while trying to load the image, url:", url)

    new_labels = []
    if labels:
        
        for label in labels:
            try: 
                len(label) == 5
            except:
                print("check the number of columns, input", label)
            x = float(label[1])
            y = float(label[2])
            w = float(label[3])
            h = float(label[4])
            newX, newY = flipLabel(x , y, flipCode)
            new_labels.append( [label[0], newX, newY , w, h] )
        
    if flipCode in [-1,0,1]:
        flipedImage = cv2.flip(image, flipCode)

        return flipedImage, new_labels
    else:
        return image, new_labels