import cv2
import winsound
import time

cam = cv2.VideoCapture(0 and 1)
while cam.isOpened():
    ret, frame1 = cam.read()
    ret, frame2 = cam.read()
    diff = cv2.absdiff(frame2, frame1)
    gray = cv2.cvtColor(diff, cv2.COLOR_RGBA2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thres = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thres, None, iterations=3)
    contros, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    for c in contros:
        if cv2.contourArea(c) < 1000:
            continue
        x, y, w, h = cv2.boundingRect(c)
        cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 0, 255), 2)
        winsound.Beep(2000,100)
    if cv2.waitKey(10) == ord("?"):
        break
    cv2.imshow("Aagaya's Camera", frame1)