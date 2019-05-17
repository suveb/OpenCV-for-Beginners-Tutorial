import cv2
import numpy as np
import matplotlib.pyplot as plt

#Storing the path of all Images in a list
imgpath = [ '..\Objects\lena_color_512.tif', '..\Objects\lbc.1.04.tiff',
            '..\Objects\l.1.01.tiff', '..\Objects\l.1.03.tiff' ]

#creating kernel for Smoothen the image
k=np.array( ( [ 1, 1, 1 ],
              [ 1, 1, 1 ],
              [ 1, 1, 1 ] ), np.float32)/9

#For loop to traverse each image of the list
for i in range(4):

    #Reading image from the list
    img = cv2.imread(imgpath[i])


    #Taking convolution of image and kernel
    smooth = cv2.filter2D(img, -1, k)


    #Converting image to RGB for representing in matplotlib
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    smooth = cv2.cvtColor(smooth, cv2.COLOR_BGR2RGB)


    #plotting origanl image and sharpen image for comparison
    plt.subplot(4,2,2*i+1)
    plt.imshow( img )
    plt.xticks([])
    plt.yticks([])
    plt.subplot(4,2,2*i+2)
    plt.imshow( smooth )
    plt.xticks([])
    plt.yticks([])


#showing image which is plotted
plt.show()