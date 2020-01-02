# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 22:37:51 2019

@author: Vivek Rathi

Shortest Path Finding using BFS
If there is no path, the function will return False
"""


import numpy as np
import cv2

# functions to traverse neighbours according to adjacency
def explore_4_neigh(r,c,A,V):
    dr = [-1,1,0,0] # direction for rows, i.e. up & down
    dc = [0,0,1,-1] # direction for columns, i.e. left & right
    for i in range(4):
        rr = r + dr[i] # update the [rr,cc] for validating the pixel location
        cc = c + dc[i]
        # use constraints to avoid considering illegal pixel locations
        if rr < 0 or cc < 0:
            continue
        if rr >= row or cc >= col:
            continue
        if visited_pixel[rr,cc]:
            continue
        if not(A[rr,cc] in V):
            continue
        # iff valid pixel locations, queue the locations [rr,cc]
        que_r.append(rr)
        que_c.append(cc)
        # keep track of visited pixel locations
        visited_pixel[rr,cc] = True
        # use global keyword to use the variable locally & globally
        global pixels_in_next_branch
        # Update pixels in next branch
        pixels_in_next_branch = pixels_in_next_branch + 1

def explore_8_neigh(r,c,A,V):
    dr = [-1,1,0,0,-1,+1,-1,1]
    dc = [0,0,1,-1,-1,-1,1,1]
    for i in range(8):
        rr = r + dr[i]
        cc = c + dc[i]
        if rr < 0 or cc < 0:
            continue
        if rr >= row or cc >= col:
            continue
        if visited_pixel [rr,cc]:
            continue
        if not(A[rr,cc] in V):
            continue
        que_r.append(rr)
        que_c.append(cc)
        visited_pixel[rr,cc] = True
        global pixels_in_next_branch
        pixels_in_next_branch = pixels_in_next_branch + 1

def explore_m_neigh(r,c,A,V):
    dr = [-1,1,0,0,-1,+1,-1,1]
    dc = [0,0,1,-1,-1,-1,1,1]
    for i in range(8):
        rr = r + dr[i]
        cc = c + dc[i]
        if rr < 0 or cc < 0:
            continue
        if rr >= row or cc >= col:
            continue
        if visited_pixel [rr,cc]:
            continue
        if not(A[rr,cc] in V):
            continue
        if rr == r - 1 and cc == c - 1 and ((A[r-1,c] in V) or (A[r,c-1] in V)):
            continue
        if rr == r + 1 and cc == c - 1 and ((A[r+1,c] in V) or (A[r,c-1] in V)):
            continue
        if rr == r - 1 and cc == c + 1 and ((A[r,c+1] in V) or (A[r-1,c] in V)):
            continue
        if rr == r + 1 and cc == c + 1 and ((A[r,c+1] in V) or (A[r+1,c] in V)):
            continue
        que_r.append(rr)
        que_c.append(cc)
        visited_pixel[rr,cc] = True
        global pixels_in_next_branch
        pixels_in_next_branch = pixels_in_next_branch + 1


def getpath(atype,mat,V):
    # Enqueque the queue with the starting pixel's row and column position
    que_r.append(sr)
    que_c.append(sc)
    # Update visited_pixel's array
    visited_pixel[sr,sc] = True
    #global declaration
    global at_end
    # do this untill my queue is empty
    while len(que_r) > 0:
        # Dequeque the queue to get values at the head of the queue
        rd = que_r.pop(0)
        cd = que_c.pop(0)
        # if we reached the end, exit the loop
        if [rd,cd] == [er,ec]:
            at_end = True
            break
        # depending on the type of adjacency, explore the neighbours
        if atype == '4':
            explore_4_neigh(rd,cd,mat,V)
        elif atype == '8':
            explore_8_neigh(rd,cd,mat,V)
        elif atype == 'm':
            explore_m_neigh(rd,cd,mat,V)
        # break/exit condition when there is no valid/legal path available
        if len(que_r) == 0:
            break
        global pixels_in_curr_branch, pixels_in_next_branch, path_steps
        # update the variable
        pixels_in_curr_branch = pixels_in_curr_branch - 1
        # if i have 0 pixels in the current branch, add the path steps and trajectory
        if pixels_in_curr_branch == 0:
            pixels_in_curr_branch = pixels_in_next_branch
            pixels_in_next_branch = 0
            path_steps = path_steps + 1
            path_pixels.append([rd,cd])
    # if we get to the end, mission accomplished, return path steps and trajectory
    if at_end:
        path_pixels.append([er,ec])
        return path_steps, path_pixels
    else:
        return False


# Main code
        
# Example 1
A = np.array(([3,1,2,1],[2,2,0,2],[1,2,1,1],[1,0,1,2]))
# get rows and columns of example matrix
row = A.shape[0]
col = A.shape[1]
V2 = [1,2] #Set 2 for neighbours adjacency
V1 = [0,1] #Set 1 for neighboiurs adjacency

# pixel locations for start pixel
sr = 3
sc = 0
# pixel locations for end pixel
er = 0
ec = 3

# define queues for rows and columns of the array i.e. pixel locations (x,y)
que_r = []
que_c = []
#path 4
# create boolean array to track visited pixels
visited_pixel = np.zeros((row,col)).astype(bool)
# define list for getting path trajectory
path_pixels = []
# counter variable for path steps
path_steps = 0
pixels_in_curr_branch = 1
pixels_in_next_branch = 0
# flag for end location
at_end = False
path4 = getpath('4',A,V1)


#path 8
que_r = [] #clear the queues
que_c = []
# create boolean array to track visited pixels
visited_pixel = np.zeros((row,col)).astype(bool)
# define list for getting path trajectory
path_pixels = []
# counter variable for path steps
path_steps = 0
pixels_in_curr_branch = 1
pixels_in_next_branch = 0
# flag for end location
at_end = False
path8 = getpath('8',A,V1)


#path m 
que_r = []
que_c = []
# create boolean array to track visited pixels
visited_pixel = np.zeros((row,col)).astype(bool)
# define list for getting path trajectory
path_pixels = []
# counter variable for path steps
path_steps = 0
pixels_in_curr_branch = 1
pixels_in_next_branch = 0
# flag for end location
at_end = False
pathm = getpath('m',A,V1)
print("Image1 = \n",A)
print("Set =",V1)
print("Path4 = ",path4)
print("Path8 = ",path8)
print("Pathm = ",pathm)
print('\n')

#path 4
que_r = []
que_c = []
# create boolean array to track visited pixels
visited_pixel = np.zeros((row,col)).astype(bool)
# define list for getting path trajectory
path_pixels = []
# counter variable for path steps
path_steps = 0
pixels_in_curr_branch = 1
pixels_in_next_branch = 0
# flag for end location
at_end = False
path4 = getpath('4',A,V2)


#path 8
que_r = []
que_c = []
# create boolean array to track visited pixels
visited_pixel = np.zeros((row,col)).astype(bool)
# define list for getting path trajectory
path_pixels = []
# counter variable for path steps
path_steps = 0
pixels_in_curr_branch = 1
pixels_in_next_branch = 0
# flag for end location
at_end = False
path8 = getpath('8',A,V2)


#path m 
que_r = []
que_c = []
# create boolean array to track visited pixels
visited_pixel = np.zeros((row,col)).astype(bool)
# define list for getting path trajectory
path_pixels = []
# counter variable for path steps
path_steps = 0
pixels_in_curr_branch = 1
pixels_in_next_branch = 0
# flag for end location
at_end = False
pathm = getpath('m',A,V2)
print("Image1 = \n",A)
print("Set =",V2)
print("Path4 = ",path4)
print("Path8 = ",path8)
print("Pathm = ",pathm)
print('\n')


##Example 2
imgrey = cv2.imread('wolves.png',0)
B = imgrey[300:305,400:405]
# get rows and columns of example matrix
row = B.shape[0]
col = B.shape[1]
V = [34,43,46]
sr = 0
sc = 0
er = 4
ec = 4
# define queues for rows and columns of the array i.e. pixel locations (x,y)
que_r = []
que_c = []

#path4
# create boolean array to track visited pixels
visited_pixel = np.zeros((row,col)).astype(bool)
# define list for getting path trajectory
path_pixels = []
# counter variable for path steps
path_steps = 0
pixels_in_curr_branch = 1
pixels_in_next_branch = 0
# flag for end location
at_end = False
path4 = getpath('4',B,V)

#path 8
que_r = []
que_c = []
# create boolean array to track visited pixels
visited_pixel = np.zeros((row,col)).astype(bool)
# define list for getting path trajectory
path_pixels = []
# counter variable for path steps
path_steps = 0
pixels_in_curr_branch = 1
pixels_in_next_branch = 0
# flag for end location
at_end = False
path8 = getpath('8',B,V)

#path m
que_r = []
que_c = []
# create boolean array to track visited pixels
visited_pixel = np.zeros((row,col)).astype(bool)
# define list for getting path trajectory
path_pixels = []
# counter variable for path steps
path_steps = 0
pixels_in_curr_branch = 1
pixels_in_next_branch = 0
# flag for end location
at_end = False
pathm = getpath('m',B,V)
print("Image2 = \n",B)
print("Set =",V)
print("Path4 = ",path4)
print("Path8 = ",path8)
print("Pathm = ",pathm)
print('\n')

#Example 3
D = imgrey[4:9,5:10]
row = D.shape[0]
col = D.shape[1]
V = [0]
sr = 0
sc = 0
er = 4
ec = 0
# define queues for rows and columns of the array i.e. pixel locations (x,y)
que_r = []
que_c = []
#path4
# create boolean array to track visited pixels
visited_pixel = np.zeros((row,col)).astype(bool)
# define list for getting path trajectory
path_pixels = []
# counter variable for path steps
path_steps = 0
pixels_in_curr_branch = 1
pixels_in_next_branch = 0
# flag for end location
at_end = False
path4 = getpath('4',D,V)

#path 8
que_r = []
que_c = []
# create boolean array to track visited pixels
visited_pixel = np.zeros((row,col)).astype(bool)
# define list for getting path trajectory
path_pixels = []
# counter variable for path steps
path_steps = 0
pixels_in_curr_branch = 1
pixels_in_next_branch = 0
# flag for end location
at_end = False
path8 = getpath('8',D,V)

#path m
que_r = []
que_c = []
# create boolean array to track visited pixels
visited_pixel = np.zeros((row,col)).astype(bool)
# define list for getting path trajectory
path_pixels = []
# counter variable for path steps
path_steps = 0
pixels_in_curr_branch = 1
pixels_in_next_branch = 0
# flag for end location
at_end = False
pathm = getpath('m',D,V)
print("Image3 = \n",D)
print("Set =",V)
print("Path4 = ",path4)
print("Path8 = ",path8)
print("Pathm = ",pathm)
print('\n')

#Example 4
E = imgrey[50:60,200:205]
row = E.shape[0]
col = E.shape[1]
V = [66,21,50]
sr = 9
sc = 4
er = 3
ec = 0
# define queues for rows and columns of the array i.e. pixel locations (x,y)
que_r = []
que_c = []
#path4
# create boolean array to track visited pixels
visited_pixel = np.zeros((row,col)).astype(bool)
# define list for getting path trajectory
path_pixels = []
# counter variable for path steps
path_steps = 0
pixels_in_curr_branch = 1
pixels_in_next_branch = 0
# flag for end location
at_end = False
path4 = getpath('4',E,V)

#path 8
que_r = []
que_c = []
# create boolean array to track visited pixels
visited_pixel = np.zeros((row,col)).astype(bool)
# define list for getting path trajectory
path_pixels = []
# counter variable for path steps
path_steps = 0
pixels_in_curr_branch = 1
pixels_in_next_branch = 0
# flag for end location
at_end = False
path8 = getpath('8',E,V)

#path m
que_r = []
que_c = []
# create boolean array to track visited pixels
visited_pixel = np.zeros((row,col)).astype(bool)
# define list for getting path trajectory
path_pixels = []
# counter variable for path steps
path_steps = 0
pixels_in_curr_branch = 1
pixels_in_next_branch = 0
# flag for end location
at_end = False
pathm = getpath('m',E,V)
print("Image4 = \n",E)
print("Set =",V)
print("Path4 = ",path4)
print("Path8 = ",path8)
print("Pathm = ",pathm)
print('\n')
