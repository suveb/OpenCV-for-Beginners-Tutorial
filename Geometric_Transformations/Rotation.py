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

    #Generating Matrix for warp affine
    R = cv2.getRotationMatrix2D( ( width/2, height/2 ), 90, 1 )

    #Generating rotated image
    rotate = cv2.warpAffine( img, R, ( width, height ) )


    #Converting image to RGB for representing in matplotlib
    img = cv2.cvtColor( img, cv2.COLOR_BGR2RGB )
    rotate = cv2.cvtColor( rotate, cv2.COLOR_BGR2RGB )


    #plotting origanl image and rotated image for comparison
    plt.subplot(4,2,2*i+1)
    plt.title('Orignal')
    plt.imshow( img )
    plt.xticks([])
    plt.yticks([])
    plt.subplot(4,2,2*i+2)
    plt.imshow( rotate )
    plt.title('Rotated')
    plt.xticks([])
    plt.yticks([])


#showing image which is plotted
plt.show()