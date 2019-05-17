# import the necessary packages
import numpy as np
import cv2
import matplotlib.pyplot as plt

def rescale_intensity(img):
    w,h=img.shape
    for i in range(w):
        for j in range(h):
            if img[i][j]>255 or img[i][j]<0:
                img[i][j]=0
    return img

def convolve(image, kernel):
	# grab the spatial dimensions of the image, along with
	# the spatial dimensions of the kernel
	(iH, iW) = image.shape[:2]
	(kH, kW) = kernel.shape[:2]

	# allocate memory for the output image, taking care to
	# "pad" the borders of the input image so the spatial
	# size (i.e., width and height) are not reduced
	pad = (kW - 1) // 2
	image = cv2.copyMakeBorder(image, pad, pad, pad, pad,
		cv2.BORDER_REPLICATE)
	output = np.zeros((iH, iW), dtype="float32")

	# loop over the input image, "sliding" the kernel across
	# each (x, y)-coordinate from left-to-right and top to
	# bottom
	for y in np.arange(pad, iH + pad):
		for x in np.arange(pad, iW + pad):
			# extract the ROI of the image by extracting the
			# *center* region of the current (x, y)-coordinates
			# dimensions
			roi = image[y - pad:y + pad + 1, x - pad:x + pad + 1]

			# perform the actual convolution by taking the
			# element-wise multiplicate between the ROI and
			# the kernel, then summing the matrix
			k = (roi * kernel).sum()

			# store the convolved value in the output (x,y)-
			# coordinate of the output image
			output[y - pad, x - pad] = k

	# loop over the input image, "sliding" the kernel across
	# each (x, y)-coordinate from left-to-right and top to
	# bottom
	for y in np.arange(pad, iH + pad):
		for x in np.arange(pad, iW + pad):
			# extract the ROI of the image by extracting the
			# *center* region of the current (x, y)-coordinates
			# dimensions
			roi = image[y - pad:y + pad + 1, x - pad:x + pad + 1]
 
			# perform the actual convolution by taking the
			# element-wise multiplicate between the ROI and
			# the kernel, then summing the matrix
			k = (roi * kernel).sum()
 
			# store the convolved value in the output (x,y)-
			# coordinate of the output image
			output[y - pad, x - pad] = k
    #rescale the output image to be in the range [0, 255]
	output = rescale_intensity(output)
	output = (output * 255).astype("uint8")
 
	# return the output image
	return output

#Storing the path of all Images in a list
imgpath = [ '..\Objects\lena_color_512.tif', '..\Objects\lbc.1.04.tiff',
            '..\Objects\l.1.01.tiff', '..\Objects\l.1.03.tiff' ]

#creating kernel for sharpen the image
k=np.array( ( [ 0, -1,  0 ],
              [-1,  5, -1 ],
              [ 0, -1,  0 ] ), np.float32)

#For loop to traverse each image of the list
for i in range(4):

    #Reading image from the list
    img = cv2.imread( imgpath[i],0 )


    #Taking convolution of image and kernel
    sharp = convolve(img,k)


    #Converting image to RGB for representing in matplotlib
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    sharp = cv2.cvtColor(sharp, cv2.COLOR_BGR2RGB)


    #plotting origanl image and sharpen image for comparison
    plt.subplot(4,2,2*i+1)
    plt.imshow( img )
    plt.xticks([])
    plt.yticks([])
    plt.subplot(4,2,2*i+2)
    plt.imshow( sharp )
    plt.xticks([])
    plt.yticks([])


#showing image which is plotted
plt.show()