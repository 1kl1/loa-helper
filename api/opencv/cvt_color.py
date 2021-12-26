import cv2


image = cv2.imread("image/sample_35.jpg", cv2.IMREAD_ANYCOLOR)
dst = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("35", image)
cv2.waitKey()
cv2.imshow("35", dst)
cv2.waitKey()
cv2.destroyAllWindows()
