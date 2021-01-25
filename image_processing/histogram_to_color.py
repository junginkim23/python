# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 16:24:42 2020

@author: USER
"""


import scipy
import numpy as np
from scipy import ndimage
from matplotlib import pyplot as plt
import cv2 

img=plt.imread('parrot_low.png')
img = np.uint8(255*img) 
 
lum_cnt=np.zeros((256,1))

h,w,z=img.shape
lumimg = img[:,:,0] * 0.2126 + img[:,:,1] * 0.7152 + img[:,:,2] * 0.0722 
lumimg=np.uint8(lumimg)

for i in range(h):
    for j in range(w):
        pixel=lumimg[i,j]
        lum_cnt[pixel,]=lum_cnt[pixel,]+1
    
pdf=lum_cnt/(h*w)

for i in range(0,255):
    pdf[i+1,]+=pdf[i,]

histo_eq_img=np.zeros([h,w])

for i in range(h):
    for j in range(w):
        pixel=lumimg[i,j]
        histo_eq_img[i,j]=round((255*(float(pdf[pixel,]))))
histo_eq=np.zeros(img.shape)
histo_eq[:,:,0]=histo_eq[:,:,1]=histo_eq[:,:,2]=histo_eq_img[:,:]
histo_eq_img1=np.uint8(histo_eq_img)


fig=plt.figure(figsize=(6,6))
a=fig.add_subplot(2,2,1)
b=fig.add_subplot(2,2,2)
c=fig.add_subplot(2,2,3)
d=fig.add_subplot(2,2,4)
a.imshow(img)
b.hist(img.flatten(),256,[0,256])
c.imshow(histo_eq_img1)
d.hist(histo_eq_img1.flatten(),256,[0,256])
plt.subplots_adjust(wspace=1,hspace=1) #간격 조절
a.set_title('original image')
b.set_title('original image histogram')
c.set_title('histogram equalization image')
d.set_title('histogram equalization histogram')
b.grid(True)
d.grid(True)
plt.show()
