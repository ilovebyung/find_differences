import numpy as np
import cv2
import os
import glob
import matplotlib.pyplot as plt

'''
get background from a video 
'''
file = 'D:/source/object_tracking/traffic.mp4'
video = cv2.VideoCapture(file)

FOI = video.get(cv2.CAP_PROP_FRAME_COUNT) * np.random.uniform(size=30)

# creating an array of frames from frames chosen above
frames = []
for frameOI in FOI:
    video.set(cv2.CAP_PROP_POS_FRAMES, frameOI)
    ret, frame = video.read()
    frames.append(frame)

# calculate the average
backgroundFrame = np.median(frames, axis=0).astype(dtype=np.uint8)
cv2.imwrite("bg.jpg", backgroundFrame)
cv2.imshow('', backgroundFrame)


# creating an array of frames from frames chosen above
images = []
files = glob.glob('D:/Data/feather/*.jpg')
for file in files:
    image = cv2.imread(file, 0)
    images.append(image)

# calculate the average
background_image = np.median(images, axis=0).astype(dtype=np.uint8)
plt.imshow(background_image, cmap='gray')

cv2.imwrite("background.jpg", backgroundFrame)
