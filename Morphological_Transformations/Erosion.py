import cv2
import numpy as np
import matplotlib.pyplot as plt

#Storing the path of the image
imgpath = '..\Objects\lena_color_512.tif'

#Reading Image from the path
img = cv2.imread( imgpath, 0 )

#Converting image to binary inverse threshold at middle value(i.e 127)
ret, bin_inv = cv2.threshold( img, 127, 255, cv2.THRESH_BINARY_INV)

#Creating Kernel for Morphological Transform
k=np.ones( ( 5, 5 ), np.uint8 )

#Erosion type Morphological Transform
erode = cv2.erode( bin_inv, k, iterations = 2 )

#Plotting image using Matplotlib
plt.subplot(1,2,1)
plt.imshow( bin_inv, cmap ='gray' )
plt.title("BinaryINV Thresh")
plt.xticks([ ])
plt.yticks([ ])

plt.subplot(1,2,2)
plt.imshow( erode, cmap ='gray' )
plt.title("Erosion")
plt.xticks([ ])
plt.yticks([ ])
plt.show()