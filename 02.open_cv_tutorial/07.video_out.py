import sys
import cv2


cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Camera open failed!")
    sys.exit()

w = round(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

fourcc = cv2.VideoWriter_fourcc(*"DIVX")  # *'DIVX' == 'D', 'I', 'V', 'X'
delay = round(1000 / fps)

out = cv2.VideoWriter("output.avi", fourcc, fps, (w, h))

if not out.isOpened():
    print("File open failed!")
    cap.release()
    sys.exit()

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # inversed = ~frame
    edge = cv2.Canny(frame, 50, 150) # 흑백 -> 컬러로 변환 필요
    edge_color = cv2.cvtColor(edge, cv2.COLOR_GRAY2BGR) # write으로 저장가능
    out.write(edge_color)

    cv2.imshow("frame", frame)
    # cv2.imshow("inversed", inversed)

    if cv2.waitKey(delay) == 27:
        break

cap.release()
out.release()
cv2.destroyAllWindows()
