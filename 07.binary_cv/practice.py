import numpy as np
import sys
import math
import cv2


def reorderPts(pts):
    idx = np.lexsort((pts[:, 1], pts[:, 0]))  # 칼럼0 -> 칼럼1 순으로 정렬한 인덱스를 반환
    pts = pts[idx]  # x좌표로 정렬

    if pts[0, 1] > pts[1, 1]:
        pts[[0, 1]] = pts[[1, 0]]

    if pts[2, 1] < pts[3, 1]:
        pts[[2, 3]] = pts[[3, 2]]

    return pts


def main():
    img = cv2.imread('namecard2.jpg', cv2.IMREAD_COLOR)

    if img is None:
        print('Image load failed!')
        return
    
    print(img.shape)
    img = cv2.resize(img, dsize=(1008, 756), interpolation=cv2.INTER_LINEAR)
    print(img.shape)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, img_bin = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    cv2.imshow('img', img_bin)
    cv2.waitKey()
    contours, _ = cv2.findContours(img_bin, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for pts in contours:
        if cv2.contourArea(pts) < 20*20:  #  너무 작으면 무시
            continue
        
        approx = cv2.approxPolyDP(pts, cv2.arcLength(pts, True)*0.02, True)
        vtc = len(approx)
        print(vtc)
        if vtc == 4:    
            print(vtc)
            print(approx.shape)
            approx = np.reshape(approx, (4, -1)).astype(np.float32)
            print(approx.shape)
            print(approx) 
            srcQuad = reorderPts(approx)  # 네 모서리 순서 정렬
            w, h = 720, 400 # 명함 크기
            dstQuad = np.array(
                [[0, 0], [0, h - 1], [w - 1, h - 1], [w - 1, 0]], np.float32)

            pers = cv2.getPerspectiveTransform(srcQuad, dstQuad)
            dst = cv2.warpPerspective(img, pers, (w, h), flags=cv2.INTER_CUBIC)

    cv2.imshow('img', img)
    cv2.imshow('dst', dst)
    cv2.waitKey()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
