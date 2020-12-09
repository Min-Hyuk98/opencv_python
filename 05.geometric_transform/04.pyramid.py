import sys
import numpy as np
import cv2


src = cv2.imread("cat.bmp")

if src is None:
    print("Image load failed!")
    sys.exit()


rc = (250, 120, 200, 200)  # rectangle tuple

# 원본 영상에 그리기
cpy = src.copy()
cv2.rectangle(cpy, rc, (0, 0, 255), 2)
cv2.imshow("src", cpy)
cv2.waitKey()

# 피라미드 영상에 그리기
for i in range(1, 4):
    src = cv2.pyrDown(src)
    #(240, 320, 3)
    #(120, 160, 3)
    #(60, 80, 3)

    cpy = src.copy()
    cv2.rectangle(cpy, rc, (0, 0, 255), 2, shift=i)# shift로 크기 조절
    cv2.imshow("src", cpy)
    cv2.waitKey()
    cv2.destroyWindow("src") # 잔상이 남지 않도록 창을 닫았다 열기

cv2.destroyAllWindows()
