import sys
import numpy as np
import cv2


# 입력 영상 불러오기
src = cv2.imread('nemo.jpg')

if src is None:
    print('Image load failed!')
    sys.exit()

# 사각형 지정을 통한 초기 분할
rc = cv2.selectROI(src)
mask = np.zeros(src.shape[:2], np.uint8)

cv2.grabCut(src, mask, rc, None, None, 5, cv2.GC_INIT_WITH_RECT)

# 0: cv2.GC_BGD, 2: cv2.GC_PR_BGD
# background면 0으로, 객체면 1로 표시
mask2 = np.where((mask == 0) | (mask == 2), 0, 1).astype('uint8')
dst = src * mask2[:, :, np.newaxis] 
mask = mask * 64 # mask는 0,1,2,3으로 이루어짐 -> 64곱하면 256픽셀 됨..
mask2 = mask2 * 64

# 초기 분할 결과 출력
cv2.imshow('mask', mask)
cv2.imshow('mask2', mask2)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()
