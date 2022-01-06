import cv2
import matplotlib.pyplot as plt

def flip_label(x, y, flipCode):
    if flipCode == 1:
        xFlipped = (1 - x)
        return xFlipped, y

    else: 
        yFlipped  = (1 - y) 
        return x, yFlipped
    


def flip_image(url, labels = None, flipCode = 0 ):
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

            newX, newY = flip_label(label[1], label[2], flipCode)
            new_labels.append( [label[0], newX, newY , label[3], label[4]] )
        
    
    flipedImage = cv2.flip(image, flipCode)

    return flipedImage, new_labels

new_img , labels= flip_image ( './test.jpg', [["men",0.68,0.52, 0.5,0.95],["men",0.2,0.5, 0.4,0.8]], 1)
cx = round(labels[0][1] * new_img.shape[1])
cy = round(labels[0][2] * new_img.shape[0])
w = labels[0][3] * new_img.shape[1]
h = labels[0][4] * new_img.shape[0]
x1 = round (cx - w/2)
y1 = round (cy - h/2)
x2 = round (cx + w/2)
y2 = round (cy + h/2)

new_img = cv2.circle(new_img, center = (cx,cy), radius=2, color = (0,0,0))
new_img = cv2.rectangle( new_img, pt1 = (x1,y1), pt2=(x2,y2), color= (0,0,0), thickness= 2)

cx = round(labels[1][1] * new_img.shape[1])
cy = round(labels[1][2] * new_img.shape[0])
w = labels[1][3] * new_img.shape[1]
h = labels[1][4] * new_img.shape[0]
x1 = round (cx - w/2)
y1 = round (cy - h/2)
x2 = round (cx + w/2)
y2 = round (cy + h/2)

new_img = cv2.circle(new_img, center = (cx,cy), radius=2, color = (0,0,255))
new_img = cv2.rectangle( new_img, pt1 = (x1,y1), pt2=(x2,y2), color= (0,0,255), thickness= 2)

print(cx,cy,w,h)
plt.imshow(new_img)
plt.show()


