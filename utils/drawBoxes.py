import cv2
import random 

def drawBoxes(image, labels):
    
    for label in labels:
        cx = round(label[1] * image.shape[1])
        cy = round(label[2] * image.shape[0])
        w = label[3] * image.shape[1]
        h = label[4] * image.shape[0]
        x1 = round (cx - w/2)
        y1 = round (cy - h/2)
        x2 = round (cx + w/2)
        y2 = round (cy + h/2)

        random_color = (random.randint(0,255) ,random.randint(0,255) ,random.randint(0,255) )

        image = cv2.putText(image, label[0], (cx - 5, cy - 5), cv2.FONT_HERSHEY_SIMPLEX, 3, random_color, 6, cv2.LINE_AA)
        image = cv2.rectangle( image, pt1 = (x1,y1), pt2 = (x2,y2), color= random_color, thickness= 4)

    return image
    #print(cx,cy,w,h)
    