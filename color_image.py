import sys
import cv2

rgb_image = cv2.imread(sys.argv[1])
print("RGB value of pixel (20, 25): " + str(rgb_image[19, 24]))
cv2.imshow("Original Image", rgb_image)

rgb_planes = cv2.split(rgb_image)
cv2.imshow("Blue", rgb_planes[0])
cv2.imshow("Green", rgb_planes[1])
cv2.imshow("Red", rgb_planes[2])

ycrcb_image = cv2.cvtColor(rgb_image, cv2.COLOR_BGR2YCrCb)
print("YCrCb value of pixel (20, 25): " + str(ycrcb_image[19, 24]))
ycrcb_planes = cv2.split(ycrcb_image)
cv2.imshow("Y", ycrcb_planes[0])
cv2.imshow("Cb", ycrcb_planes[1])
cv2.imshow("Cr", ycrcb_planes[2])

hsv_image = cv2.cvtColor(rgb_image, cv2.COLOR_BGR2HSV)
print("HSV value of pixel (20, 25): " + str(hsv_image[19, 24]))
hsv_planes = cv2.split(hsv_image)
cv2.imshow("Hue", hsv_planes[0])
cv2.imshow("Saturation", hsv_planes[1])
cv2.imshow("Value", hsv_planes[2])

cv2.waitKey(0)
