import cv2

image = cv2.imread("image/sample_35.jpg", cv2.IMREAD_ANYCOLOR)
# cv2.IMREAD_UNCHANGED : 원본 사용
# cv2.IMREAD_ANYCOLOR : 가능한 3 채널, 색상 이미지로 사용
# cv2.IMREAD_GRAYSCALE : 1 채널, 그레이스케일 적용

cv2.imshow("35", image)
height, width, channel = image.shape
print(height, width, channel)
cv2.waitKey()
cv2.destroyAllWindows()
