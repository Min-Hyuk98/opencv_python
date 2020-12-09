import sys
import cv2
print(sys.path)
print('open_cv version:', cv2.__version__)

img = cv2.imread('c:\\Users\\82109\\open_cv\\opencv_python_ch01_ch05\\ch01\\cat.bmp', cv2.IMREAD_GRAYSCALE)
# img = cv2.imread('ch01/cat.bmp', cv2.IMREAD_GRAYSCALE)

if img is None:
    print("image load failed")
    sys.exit() 

cv2.imwrite('cat_gray.png', img)

cv2.namedWindow('image')
cv2.imshow('image', img)

while True:
    if cv2.waitKey() == 27: # ESC 눌렀을 때만 종료
        break
    
cv2.destroyAllWindows()
