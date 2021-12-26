import cv2

src = cv2.imread("image/sample_35.jpg", cv2.IMREAD_ANYCOLOR)
dst = cv2.bitwise_not(src)

cv2.imshow("35", dst)
cv2.waitKey()
cv2.destroyAllWindows()
