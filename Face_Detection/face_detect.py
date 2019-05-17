import cv2
import matplotlib.pyplot as plt

#Haar Cascade Path
haarPath = '..\Objects\haarcascade_frontalface_default.xml'


#All Imgages Path
imgpath = [ '..\Objects\lena_color_512.tif', '..\Objects\lbc.1.04.tiff',
            '..\Objects\l.1.01.tiff', '..\Objects\l.1.03.tiff' ]


#Reading Haar Cascade
faceData = cv2.CascadeClassifier( haarPath )


#For each image
for i in range(4):

    #Reading image and converting to gray
    img = cv2.imread( imgpath[i] )
    gray = cv2.cvtColor( img, cv2.COLOR_BGR2GRAY )


    #detecting first point, width and height
    points = faceData.detectMultiScale( img, 1.05, 6 )


    #Creating multiple box for multiple person in a single image
    for a,b,c,d in points:
        cv2.rectangle( img, ( a, b ), ( a+c, b+d ), ( 0, 0, 255 ), 2 )


    #converting to RGB for displaying through matplotlib
    img = cv2.cvtColor( img, cv2.COLOR_BGR2RGB )


    #plotting image
    plt.subplot(2,2,i+1)
    plt.imshow(img)


#showing image through matplotlib
plt.show()
