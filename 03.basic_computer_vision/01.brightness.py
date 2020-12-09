import sys
import numpy as np
import cv2


# 그레이스케일 영상 불러오기
src = cv2.imread("lenna.bmp", cv2.IMREAD_GRAYSCALE)

if src is None:
    print("Image load failed!")
    sys.exit()

print(cv2.add(2, 3))
dst = cv2.add(src, 100) # (100,0,0,0)
# dst = src + 100 # 이런식으로 하면 uint8초과되는 값 잘못됨
# dst = np.clip(src + 100., 0, 255).astype(np.uint8)


cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.waitKey()

# 컬러 영상 불러오기
src = cv2.imread("lenna.bmp")

if src is None:
    print("Image load failed!")
    sys.exit()

dst = cv2.add(src, (100, 100, 100, 0)) # B,G,R,alpha
# dst = np.clip(src + 100., 0, 255).astype(np.uint8)

cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.waitKey()

cv2.destroyAllWindows()
