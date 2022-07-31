import numpy as np #pip install numpy
import imageio #pip install imageio
import scipy.ndimage #pip install scipy
import cv2 #pip install opencv-python

img = "./Github-Projects/Beginner-Python-Projects/Sketch/Photo.jpg" # Set image location

def rgb2gray(rgb):
    return np.dot(rgb[...,:3],[0.2989,0.5870,0.1140])

def dodge(front,back):
    final_sketch = front*255/(255-back)
    final_sketch[final_sketch>255]=255
    final_sketch[back==255]=255
    return final_sketch.astype('uint8')

ss = imageio.imread(img)
gray = rgb2gray(ss)

i= 255-gray

blur = scipy.ndimage.filters.gaussian_filter(i,sigma = 15)
r = dodge(blur,gray)

cv2.imwrite('./Github-Projects/Beginner-Python-Projects/Sketch/Photo-Sketch.png',r) # Set output location