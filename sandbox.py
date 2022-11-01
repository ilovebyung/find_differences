import cv2
import numpy as np
from matplotlib import pyplot as plt

file_01 = '00.jpg'
file_02 = '01.jpg'

image_01 = cv2.imread(file_01,0)
image_02 = cv2.imread(file_02,0)

plt.imshow(image_01, cmap='gray')
plt.imshow(image_02, cmap='gray')

diff_img = cv2.subtract(image_01, image_02)
plt.imshow(diff_img, cmap='gray')

diff_img = cv2.subtract(image_02, image_01)
plt.imshow(diff_img, cmap='gray')

bg = np.zeros((1,65), int)
fg = np.zeros((1,65), int)

rect = (161,79,150,150)