import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

while True: 


    ret, frame = cap.read()
    
    if not ret:
        break
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    black_red = np.array([165, 50,50])
    light_red= np.array([179,255,255])

    mask = cv.inRange(hsv, black_red, light_red)

    result = cv.bitwise_and(frame, frame , mask= mask)

    #cv.imshow("camera original", frame)
    cv.imshow("Camear com fitro", result)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv.destroyAllWindows()