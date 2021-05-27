import cv2
import numpy as np
# from google.colab.patches import cv2_imshow
from skimage import io

img = cv2.imread("imagenes/prueba.jpg")
io.imshow(img)

img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
io.imshow(img)

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray,5)
edges = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,9,9)
io.imshow(edges)
io.imsave("imagenes/Foto_edges.jpeg",edges)

color = cv2.bilateralFilter(img,9,250,250)
cartoon = cv2.bitwise_and(color, color, mask=edges)

io.imshow(cartoon)
io.imsave("imagenes/Foto_cartoon.jpeg",cartoon)

cv2.waitKey(0)