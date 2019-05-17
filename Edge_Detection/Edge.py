import cv2
import matplotlib.pyplot as plt


#Storing the path of all Images in a list
imgpath = [ '..\Objects\lena_color_512.tif', '..\Objects\lbc.1.04.tiff',
            '..\Objects\l.1.01.tiff', '..\Objects\l.1.03.tiff' ]


#For loop to traverse each image of the list
for i in range(4):

    #Reading image from the list
    img = cv2.imread(imgpath[i], 0)


    #Using canny edge detector to detect the edges from the image
    edge = cv2.Canny( img, 55, 117, L2gradient = True )


    #plotting image using matplotlib
    plt.subplot(4,2,2*i+1)
    plt.imshow( img, cmap = 'gray' )
    plt.xticks([])
    plt.yticks([])
    plt.subplot(4,2,2*i+2)
    plt.imshow( edge, cmap = 'gray' )
    plt.xticks([])
    plt.yticks([])


#showing image which is plotted
plt.show()