# IMAGE resizer

import cv2


image = cv2.imread("book.jpg" , cv2.IMREAD_UNCHANGED)
cv2.imshow("title", image)
# cv2.waitKey(0)

scale_perc = 50

# to calculate the 50% percent of the orignal dimension
new_widht = int(image.shape[1] * scale_perc / 100)
new_height = int(image.shape[0] * scale_perc / 100)


# desize
# desize (new_widht , new_heightheight)


# resize

output= cv2.resize(image , (new_widht , new_height))
cv2.imwrite('new_imag.jpg' , output)
cv2.waitKey(0)































src = cv2.imread('aladeen .jpg' , cv2.IMREAD_UNCHANGED)
cv2.imshow('title' ,src )
cv2.waitKey(0)