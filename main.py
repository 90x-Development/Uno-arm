import cv2
import numpy as np
import time
from angle import calculate_angle
from control import base_turn


def empty(a):
    pass

def stackImages(scale, imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range(0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape[:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2:
                    imgArray[x][y] = cv2.cvtColor(imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank] * rows
        hor_con = [imageBlank] * rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None, scale, scale)
            if len(imgArray[x].shape) == 2:
                imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor = np.hstack(imgArray)
        ver = hor
    return ver

cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars", 640, 240)
cv2.createTrackbar("Hue Min", "TrackBars", 83, 179, empty)
cv2.createTrackbar("Hue Max", "TrackBars", 104, 179, empty)
cv2.createTrackbar("Sat Min", "TrackBars", 60, 255, empty)
cv2.createTrackbar("Sat Max", "TrackBars", 188, 255, empty)
cv2.createTrackbar("Val Min", "TrackBars", 49, 255, empty)
cv2.createTrackbar("Val Max", "TrackBars", 82, 255, empty)

video = cv2.VideoCapture(0)
video.set(3, 640)
video.set(4, 480)

while True:
    time.sleep(.249)
    success, img = video.read()
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("Hue Min", "TrackBars")
    h_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
    s_min = cv2.getTrackbarPos("Sat Min", "TrackBars")
    s_max = cv2.getTrackbarPos("Sat Max", "TrackBars")
    v_min = cv2.getTrackbarPos("Val Min", "TrackBars")
    v_max = cv2.getTrackbarPos("Val Max", "TrackBars")
    print(h_min, h_max, s_min, s_max, v_min, v_max)
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(imgHSV, lower, upper)
    imgResult = cv2.bitwise_and(img, img, mask=mask)
    

    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    position = None
    if len(contours) > 0:

        largest_contour = max(contours, key=cv2.contourArea)

        x, y, w, h = cv2.boundingRect(largest_contour)
        position = (x, y, w, h)

        cv2.rectangle(imgResult, (x, y), (x + w, y + h), (0, 255, 0), 2)
        

        center_x = x + w // 2 #angle_degrees
        center_y = y + h // 2
        cv2.line(imgResult,(center_x,0),(center_x,center_y),(255,0,10),1)
       # cv2.line(imgResult,(center_x,0),(480,center_y),(255,0,10),1)
        cv2.line(imgResult,(640//2,0),(640//2,480),(255,0,10),3)
        cv2.line(imgResult,(0,480//2),(640,480//2),(0,255,10),3)
       # cv2.line(img,(640//2,0),(640//2,480),(255,0,10),3)
        cv2.line(img,(100,0),(100,480),(255,0,10),3)
        cv2.line(img,(0,480//2),(640,480//2),(0,255,10),3)
        cv2.line(img,(100,240),(center_x,center_y),(0,255,10),3)
        m, n, y, r, x, z = 100,240,100,420,center_x,center_y
        cv2.line(img,(m,n),(y,r),(0,100,10),3)
        cv2.line(img,(m,n),(x,z),(0,100,10),3)
        angle =calculate_angle(m, n, x, z ,y, r)
        print(angle)
        cv2.putText(img,str(angle),(300,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,150,0),1)
        base_turn(angle)
    imgStack = stackImages(0.6, ([img, imgHSV], [mask, imgResult]))
    cv2.imshow("Stacked Images", imgStack)

    if position is not None:
        print("Position:", position)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
