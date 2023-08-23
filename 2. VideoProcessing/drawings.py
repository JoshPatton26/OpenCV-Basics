import cv2
import random
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))
    
    # This line is drawing a green line from top left to bottom right of 'frame'
    # !!  line() documentation:  !!
    # line(source image, starting pos, ending pos, color, line thickness)
    img = cv2.line(frame, (0,0), (width, height), (0, 255, 0), 10)
    # This line is drawing a blue line from bottom left to top right of 'img'
    img = cv2.line(img, (0,height), (width, 0), (255, 0, 0), 5)
    
    
    # Drawing rectangle on 'img'
    # !!  rectangle() documentation:  !!
    # rectangle(source image, center pos, radius, color, line thickness(-1 to fill))
    img = cv2.rectangle(img, (100,100), (200,200), (128, 128, 128), 5)


    # Drawing a circle on 'img'
    # !!  circle() documentation:  !!
    # circle(source image, center pos, radius, color, line thickness(-1 to fill))
    img = cv2.circle(img, (300,300), 60, (0, 0, 128), -1)

    # Draw text onto 'img'
    # !!  putText() documentation:  !!
    # circle(source image, text to diaplay, center pos, font, font scale, color, line thickness, line type = cv2.LINE_AA)
    font = cv2.FONT_HERSHEY_SIMPLEX
    img = cv2.putText(img, 'Josh is Great!', (200, height-10), font, 1, (255,255,255), 2, cv2.LINE_AA)

    cv2.imshow('frame', img)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()