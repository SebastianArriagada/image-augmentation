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

new_img , labels= flip_image ( './test.jpg', [["men",0.3,0.6, 0.1,0.2]], 1)
print(labels)
plt.imshow(new_img)
plt.show()


