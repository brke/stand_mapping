#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 13:23:49 2020

@author: Brenda


    Develop a notebook that reads in a multichannel image (e.g., RGB) experiment
    with super pixel (e.g., SLIC)
    and region-merging (e.g., Felzenswalb) algorithms in skimage.

"""

import os

filename = os.path.join(r'/Users/Brenda/Documents/IMG-9438.JPG')

    
def img_reader(filename):
    '''
    splits filename (an image file) into its RGB components
    '''     
    import matplotlib.pyplot as plt
    from skimage import io

    im = io.imread(filename)
    
    #split into RGB components and show
    im_r = im.copy()
    im_r[:,:,1]=0
    im_r[:,:,2]=0
    
    im_g = im.copy()
    im_g[:,:,0]=0
    im_g[:,:,2]=0
    
    im_b = im.copy()
    im_b[:,:,0]=0
    im_b[:,:,1]=0
    
    fig,ax = plt.subplots(ncols=4)
    
    for a in ax:
            a.axis('off')
    
    ax[0].imshow(im)
    ax[1].imshow(im_r)
    ax[2].imshow(im_g)
    ax[3].imshow(im_b)
    
    return fig

#%%

#starting to look at SLIC, tutorial found at https://www.pyimagesearch.com/2014/07/28/a-slic-superpixel-tutorial-using-python/
from skimage import io
import matplotlib.pyplot as plt
from skimage.segmentation import slic, mark_boundaries

im = io.imread(filename)
im_slic = slic(im, n_segments = 50)

fig1, ax = plt.subplots(ncols=2,dpi=300)
for a in ax:
    a.axis('off')
ax[0].imshow(mark_boundaries(im,im_slic,color=(1,0,0))) #don't know how to make lines thicker on segmented part
ax[1].imshow(im_slic)