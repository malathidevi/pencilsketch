import cv2
image = cv2.imread("lusuuuu.jpg")
grey_filter = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
invert = cv2.bitwise_not(grey_filter)
blue = cv2.GaussianBlur(invert,(21,21),0)
invertedblur = cv2.bitwise_not(blue)
sketch_filter  =cv2.divide(grey_filter, invertedblur,scale=256.0)
cv2.imwrite("output6.jpg",sketch_filter)
cv2.imwrite("output6.jpg",sketch_filter)