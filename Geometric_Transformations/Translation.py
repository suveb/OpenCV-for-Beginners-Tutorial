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


    #It will create a matrix which is used to translate the image
    T = np.float32( [ [ 1, 0, 50 ], [ 0, 1 , 50 ] ] )

    #This will translate the image with amount given by the matrix
    trans=cv2.warpAffine( img, T, ( width + 50 , height + 50 ) )


    #Converting image to RGB for representing in matplotlib
    img = cv2.cvtColor( img, cv2.COLOR_BGR2RGB )
    trans = cv2.cvtColor( trans, cv2.COLOR_BGR2RGB )


    #plotting origanl image and rotated image for comparison
    plt.subplot(4,2,2*i+1)
    plt.title('Orignal')
    plt.imshow( img )
    plt.xticks([])
    plt.yticks([])
    plt.subplot(4,2,2*i+2)
    plt.imshow( trans )
    plt.title('Trans')
    plt.xticks([])
    plt.yticks([])


#showing image which is plotted
plt.show()