import cv2
import matplotlib.image as mpimg
import numpy as np
#from moviepy.editor import VideoFileClip
import imageio


img = cv2.imread('/home/python/video2char/test2.jpg',3)
codelib = '''@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`'. '''

def image_process(image):
    txt=''
    im_gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    [m,n]= im_gray.shape  
    h=int(m/4)
    w=int(n/4)
    im_graymini = cv2.resize(im_gray,(h,w))

    length = len(codelib)
    unit = 257.0/length
    for i in range(h):
        for j in range(w):
            txt += codelib[int(im_graymini[j,i]/unit)]
        txt += '\n'
    return im_graymini,txt
    


    




mini,charmap = image_process(img)
