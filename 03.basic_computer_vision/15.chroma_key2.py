import numpy as np
import sys
import cv2

def open_vid(fn):
    vid = cv2.VideoCapture(fn)
    if not vid.isOpened():
        print('video open failed')
        sys.exit()
    return vid

cam = open_vid(0)
background = open_vid('raining.mp4')

h = round(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))
w = round(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
print(w, h)

fps_cam = cam.get(cv2.CAP_PROP_FPS)
fps_background = cam.get(cv2.CAP_PROP_FPS)
delay = int(1000/fps_cam)
print('fps_cam:', fps_cam)
print('fps_background:', fps_background)
print('delay:', delay)

do_composit = False

while True:
    ret_cam, frame_cam = cam.read()
    if not ret_cam:
        break

    if do_composit:
        ret_background, frame_background = background.read()
        if not ret_background:
            break

        frame_background = cv2.resize(frame_background, (w,h))

        hsv = cv2.cvtColor(frame_cam, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, (0, 0, 98), (255, 255, 255))
        cv2.copyTo(frame_background, mask, frame_cam)

    cv2.imshow('frame', frame_cam)
    key = cv2.waitKey(delay)

    if key == ord(" "):
        do_composit = not do_composit
    elif key == 27:
        break

cam.release()
background.release()
cv2.destroyAllWindows()