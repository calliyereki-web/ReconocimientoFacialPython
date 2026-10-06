import cv2
import os
import imutils

personName = input("Enter your name: ")
dataPath = 'C:/Users/Dell/Documents/GitHub/ReconocimientoFacialPython'
personPath = dataPath + '/' + personName

######################################################################
if not os.path.exists(personPath):
    print('Carpeta creada: ', personPath)
    os.makedirs(personPath)
######################################################################


cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) == 27:
        break
        
