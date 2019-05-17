import cv2
import numpy as np
import matplotlib.pyplot as plt

#Storing the path of all Images in a list
imgpath = [ '..\Objects\lena_color_512.tif', '..\Objects\lbc.1.04.tiff',
            '..\Objects\l.1.01.tiff', '..\Objects\l.1.03.tiff' ]


#For loop to traverse each image of the list
for i in range(4):

    #Reading image from the list
    img = cv2.imread( imgpath[i] )

    #Calculating the dimensions of image
    width, height, channel = img.shape

    #Reszing the image to 1.3 times in x and 1.8 times in y its initial value
    resize = cv2.resize( img, None, fx = 1.3, fy = 1.8 )

    #Converting image to RGB for representing in matplotlib
    img = cv2.cvtColor( img, cv2.COLOR_BGR2RGB )
    resize = cv2.cvtColor( resize, cv2.COLOR_BGR2RGB )

    #plotting orignal image and rotated image for comparison
    plt.subplot(4,2,2*i+1)
    plt.title('Orignal')
    plt.imshow( img )
    plt.xticks([])
    plt.yticks([])
    plt.subplot(4,2,2*i+2)
    plt.imshow( resize )
    plt.title('Scaled')
    plt.xticks([])
    plt.yticks([])


#showing image which is plotted
plt.show()