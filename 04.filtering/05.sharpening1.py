import sys
import numpy as np
import cv2

src = cv2.imread("rose.bmp", cv2.IMREAD_GRAYSCALE)

if src is None:
    print("Image load failed!")
    sys.exit()

blr = cv2.GaussianBlur(src, (0, 0), 2)
# dst = np.clip(2.0 * src - blr, 0, 255).astype(np.uint8)
dst = cv2.addWeighted(src, 2, blr, -1, 0)

cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.waitKey()

cv2.destroyAllWindows()
