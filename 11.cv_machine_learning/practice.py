import sys
import numpy as np
import cv2


def norm_img(img):
    h, w = img.shape[:2]

    img = ~img
    blr = cv2.GaussianBlur(img, (0, 0), 2)

    sf = 14. / h  # scale factor. 위/아래 3픽셀씩 여백 고려.
    if w > h:
        sf = 14. / w

    img2 = cv2.resize(img, (0, 0), fx=sf, fy=sf, interpolation=cv2.INTER_AREA)
    h2, w2 = img2.shape[:2]
    a = (20 - w2) // 2
    b = (20 - h2) // 2

    dst = np.zeros((20, 20), dtype=np.uint8)
    dst[b:b+h2, a:a+w2] = img2[:, :]
    
    cv2.imshow('img2', img2)
    cv2.waitKey()
    return dst


src = cv2.imread('handwritten1.png')

if src is None:
    print('image load failed')
    sys.exit()

hog = cv2.HOGDescriptor((20, 20), (10, 10), (5, 5), (5, 5), 9)
svm = cv2.ml.SVM_load('svmdigits.yml')

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
_, src_bin = cv2.threshold(src_gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)

cnt, _, stats, _ = cv2.connectedComponentsWithStats(src_bin)
dst = src.copy()
print(cnt)
print(stats.shape)

for i in range(1, cnt):
    x, y, w, h, s = stats[i]

    if s < 100:
        continue

    digit = norm_img(src_gray[y:y+h, x:x+w])
    test_desc = hog.compute(digit).T
    _, res = svm.predict(test_desc)

    # HOG&SVM 숫자 인식 결과 출력
    cv2.rectangle(dst, (x, y, w, h), (0, 0, 255))
    cv2.putText(dst, str(int(res[0, 0])), (x, y - 5),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)

cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()
