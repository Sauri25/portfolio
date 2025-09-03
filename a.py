import cv2

img=cv2.imread("IMG_20250903_135431.jpg")

H,W=img.shape[:2]
print(H,W)

w=900
h=int((H/W)*w)
print(h)

img1=cv2.resize(img,(w,h),interpolation=cv2.INTER_CUBIC)
cv2.imshow("i",img1)
cv2.waitKey(0)
cv2.destroyAllWindows()