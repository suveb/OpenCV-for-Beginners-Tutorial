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

    #points on input and outut image
    pointI = np.float32( [ [ 0, 0 ], [ 300, 0 ], [ 150, 300 ], [ 300, 300 ] ] )
    pointO = np.float32( [ [ 0, 0 ], [ 350, 0 ], [ 0, 350 ], [ 350, 350 ] ] )

    #It is used to create matrix for image to output mapping
    P=cv2.getPerspectiveTransform(pointI,pointO)

    #This will transform the image to given perspective
    pers=cv2.warpPerspective(img,P,(width,height))

    #Converting image to RGB for representing in matplotlib
    img = cv2.cvtColor( img, cv2.COLOR_BGR2RGB )
    pers = cv2.cvtColor( pers, cv2.COLOR_BGR2RGB )

    #plotting orignal image and rotated image for comparison
    plt.subplot(4,2,2*i+1)
    plt.title('Orignal')
    plt.imshow( img )
    plt.xticks([])
    plt.yticks([])
    plt.subplot(4,2,2*i+2)
    plt.imshow( pers )
    plt.title('Output')
    plt.xticks([])
    plt.yticks([])


#showing image which is plotted
plt.show()