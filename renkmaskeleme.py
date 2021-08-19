import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)


def finder():
    global a

    a = 0
    for i in range(480):
        for j in range(640):
            if(mask[i, j] == 255):
                a = 1

            break
        continue


def Nothing(x):
    pass


cv.namedWindow("Trackbar")
cv.resizeWindow("Trackbar", 500, 500)

cv.createTrackbar("Lower - H", "Trackbar", 0, 180, Nothing)
cv.createTrackbar("Lower - S", "Trackbar", 0, 255, Nothing)
cv.createTrackbar("Lower - V", "Trackbar", 0, 255, Nothing)

cv.createTrackbar("Upper - H", "Trackbar", 0, 180, Nothing)
cv.createTrackbar("Upper - S", "Trackbar", 0, 255, Nothing)
cv.createTrackbar("Upper - V", "Trackbar", 0, 255, Nothing)


cv.setTrackbarPos("Upper - H", "Trackbar", 180)
cv.setTrackbarPos("Upper - S", "Trackbar", 255)
cv.setTrackbarPos("Upper - V", "Trackbar", 255)

while True:
    ret, frame = cap.read()
    frame = cv.flip(frame, 1)

    framehsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    lowerh = cv.getTrackbarPos("Lower - H", "Trackbar")
    lowers = cv.getTrackbarPos("Lower - S", "Trackbar")
    lowerv = cv.getTrackbarPos("Lower - V", "Trackbar")

    upperh = cv.getTrackbarPos("Upper - H", "Trackbar")
    uppers = cv.getTrackbarPos("Upper - S", "Trackbar")
    upperv = cv.getTrackbarPos("Upper - V", "Trackbar")

    lowercolor = np.array([lowerh, lowers, lowerv])
    uppercolor = np.array([upperh, uppers, upperv])

    mask = cv.inRange(framehsv, lowercolor, uppercolor)
    finder()
    cv.imshow("Orginal", frame)
    cv.imshow("mask", mask)

    if(a == 1):
        print("bib")

    if cv.waitKey(1) & 0xFF == ord("q"):
        break
print(frame.shape)

cap.release()
cv.destroyAllWindows()
