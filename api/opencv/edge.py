import cv2

src = cv2.imread("image/test_lined.bmp", cv2.IMREAD_ANYCOLOR)
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
gray = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY)[1]

sobel = cv2.Sobel(gray, cv2.CV_8U, 1, 0, 3)
laplacian = cv2.Laplacian(gray, cv2.CV_8U, ksize=3)
canny = cv2.Canny(src, 100, 255)

cv2.imshow("gray", gray)
cv2.imshow("sobel", sobel)
cv2.imshow("laplacian", laplacian)
cv2.imshow("canny", canny)
cv2.waitKey()
cv2.destroyAllWindows()
