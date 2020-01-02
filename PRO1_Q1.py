
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 13:25:13 2019

@author: Vivek Rathi

Here Neighbours are
[ Dlu vu Dru]
[ hl  P  hr ]
[ Dld vd Drd]
"""
import numpy as np
import cv2
import matplotlib.pyplot as plt

# Load image
imgrey = cv2.imread('wolves.png',0) #greyscale
ibgr = cv2.imread('wolves.png') # rgb
ihsv = cv2.cvtColor(ibgr, cv2.COLOR_BGR2HSV) #hsv
ilab = cv2.cvtColor(ibgr, cv2.COLOR_BGR2Lab) #lab

'''
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
#case 1 - intensity
def diff_2d(img_mat,nb):
    r = img_mat.shape[0]
    c = img_mat.shape[1]
    a = np.array(imgrey, dtype = 'int32')
    d = np.zeros((r,c), dtype = 'int32')
    for i in range(r):
        for j in range(c):
            if nb == 'hr':
                if [i,j] == [i,c-1]:
                    pass
                else:
                    d[i,j] = (a[i,j] - a[i,j+1])**2
            elif nb == 'vd': # x,y  x+1,y
                if [i,j] == [r-1,j]:
                    pass
                else:
                    d[i,j] = (a[i,j] - a[i+1,j])**2
            elif nb == 'vu': # x,y  x-1,y
                if [i,j] == [0,j]:
                    pass
                else:
                    d[i,j] = (a[i,j] - a[i-1,j])**2
            elif nb == 'hl': # x,y  x,y-1
                if [i,j] == [i,0]:
                    pass
                else:
                    d[i,j] = (a[i,j] - a[i,j-1])**2
            elif nb == 'Dru': # x,y  x-1,y+1
                if [i,j] == [0,j] or [i,j] == [i,c-1]:
                    pass
                else:
                    d[i,j] = (a[i,j] - a[i-1,j+1])**2
            elif nb == 'Drd': # x,y  x+1,y+1
                if [i,j] == [r-1,j] or [i,j] == [i,c-1]:
                    pass
                else:
                    d[i,j] = (a[i,j] - a[i+1,j+1])**2
            elif nb == 'Dlu': # x,y  x-1,y-1
                if [i,j] == [0,j] or [i,j] == [i,0]:
                    pass
                else:
                    d[i,j] = (a[i,j] - a[i-1,j-1])**2
            elif nb == 'Dld': # x,y  x+1,y-1
                if [i,j] == [i,0] or [i,j] == [r-1,j]:
                    pass
                else:
                    d[i,j] = (a[i,j] - a[i+1,j-1])**2
    if nb == 'hr':
        d = d[:,:c-1]
    elif nb == 'vd':
        d = d[:r-1,:]
    elif nb == 'vu':
        d = d[1:,:]
    elif nb == 'hl':
        d = d[:,1:]
    elif nb == 'Dru':
        d = d[1:,:c-1]
    elif nb == 'Drd':
        d = d[:r-1,:c-1]
    elif nb == 'Dlu':
        d = d[:r-1,1:]
    elif nb == 'Dld':
        d = d[1:,1:]
        
    return d

#case 2 3 channels
def diff_3d(img_mat,nb):
    r = img_mat.shape[0]
    c = img_mat.shape[1]
    ch1 = np.array((img_mat[:,:,0]), dtype = 'int32')
    ch2 = np.array((img_mat[:,:,1]), dtype = 'int32')
    ch3 = np.array((img_mat[:,:,2]), dtype = 'int32')
    d = np.zeros((r,c), dtype = 'int32')
    for i in range(r):
        for j in range(c):
            if nb == 'hr':
                if [i,j] == [i,c-1]:
                    pass
                else:
                    d[i,j] = (ch1[i,j] - ch1[i,j+1])**2 + (ch2[i,j] - ch2[i,j+1])**2 + (ch3[i,j] - ch3[i,j+1])**2
            elif nb == 'vd': # x,y  x+1,y
                if [i,j] == [r-1,j]:
                    pass
                else:
                    d[i,j] = (ch1[i,j] - ch1[i+1,j])**2 + (ch2[i,j] - ch2[i+1,j])**2 + (ch3[i,j] - ch3[i+1,j])**2
            elif nb == 'vu': # x,y  x-1,y
                if [i,j] == [0,j]:
                    pass
                else:
                    d[i,j] = (ch1[i,j] - ch1[i-1,j])**2 + (ch2[i,j] - ch2[i-1,j])**2 + (ch3[i,j] - ch3[i-1,j])**2
            elif nb == 'hl': # x,y  x,y-1
                if [i,j] == [i,0]:
                    pass
                else:
                    d[i,j] = (ch1[i,j] - ch1[i,j-1])**2 + (ch2[i,j] - ch2[i,j-1])**2 + (ch3[i,j] - ch3[i,j-1])**2
            elif nb == 'Dru': # x,y  x-1,y+1
                if [i,j] == [0,j] or [i,j] == [i,c-1]:
                    pass
                else:
                    d[i,j] = (ch1[i,j] - ch1[i-1,j+1])**2 + (ch2[i,j] - ch2[i-1,j+1])**2 + (ch3[i,j] - ch3[i-1,j+1])**2
            elif nb == 'Drd': # x,y  x+1,y+1
                if [i,j] == [r-1,j] or [i,j] == [i,c-1]:
                    pass
                else:
                    d[i,j] = (ch1[i,j] - ch1[i+1,j+1])**2 + (ch2[i,j] - ch2[i+1,j+1])**2 + (ch3[i,j] - ch3[i+1,j+1])**2
            elif nb == 'Dlu': # x,y  x-1,y-1
                if [i,j] == [0,j] or [i,j] == [i,0]:
                    pass
                else:
                    d[i,j] = (ch1[i,j] - ch1[i-1,j-1])**2 + (ch2[i,j] - ch2[i-1,j-1])**2 + (ch3[i,j] - ch3[i-1,j-1])**2
            elif nb == 'Dld': # x,y  x+1,y-1
                if [i,j] == [i,0] or [i,j] == [r-1,j]:
                    pass
                else:
                    d[i,j] = (ch1[i,j] - ch1[i+1,j-1])**2 + (ch2[i,j] - ch2[i+1,j-1])**2 + (ch3[i,j] - ch3[i+1,j-1])**2
    if nb == 'hr':
        d = d[:,:c-1]
    elif nb == 'vd':
        d = d[:r-1,:]
    elif nb == 'vu':
        d = d[1:,:]
    elif nb == 'hl':
        d = d[:,1:]
    elif nb == 'Dru':
        d = d[1:,:c-1]
    elif nb == 'Drd':
        d = d[:r-1,:c-1]
    elif nb == 'Dlu':
        d = d[:r-1,1:]
    elif nb == 'Dld':
        d = d[1:,1:]
        
    return d
#histogram
def histogram(img,bins,title):
    plt.hist(img.ravel(),bins);
    plt.title(title)
    plt.xlabel('Pixel Values')
    plt.ylabel('Number of Pixels')
    plt.show()
#case 1 - intensity
g1 = diff_2d(imgrey,'hl')
g2 = diff_2d(imgrey,'vu')
#case 2 - RGB
bgr1 = diff_3d(ibgr,'hr')
bgr2 = diff_3d(ibgr,'vd')
#case 3- hsv
hsv1 = diff_3d(ihsv,'Dlu')
hsv2 = diff_3d(ihsv,'Dru')
#case 4 - Lab
lab1 = diff_3d(ilab,'Dld')
lab2 = diff_3d(ilab,'Drd')
# calculate histogram 

histogram(g1,25,'Histogram for Greyscale (N = hl)')
histogram(g2,25,'Histogram for Greyscale (N = vu)')

histogram(bgr1,25,'Histogram for RGB (N = hr)')
histogram(bgr2,25,'Histogram for RGB (N = vd)')

histogram(hsv1,25,'Histogram for HSV (N = Dlu)')
histogram(hsv2,25,'Histogram for HSV (N = Dru)')

histogram(lab1,25,'Histogram for Lab (N = Dld)')
histogram(lab2,25,'Histogram for Lab (N = Drd)')