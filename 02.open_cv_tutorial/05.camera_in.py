import sys
import cv2


# 카메라 열기
cap = cv2.VideoCapture(0)
# cap = cv2.VideoCapture()
# cap.open(0)

if not cap.isOpened():
    print("Camera open failed!")
    sys.exit()

# 카메라 프레임 크기 출력
print("Frame width:", int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)))
print("Frame height:", int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

# 카메라 프레임 크기 설정
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

# 카메라 프레임 처리
while True:
    ret, frame = cap.read()

    if not ret:
        break

    inversed = ~frame  # 반전
    
    edge = cv2.Canny(frame, 50, 150)

    cv2.imshow("frame", frame)
    cv2.imshow("inversed", inversed)
    cv2.imshow("edge", edge)

    if cv2.waitKey(10) == 27:
        break

cap.release()
cv2.destroyAllWindows()
