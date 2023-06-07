#'''Instalacion de opencv en vscode'''

import cv2
#'''0 camaranativa y 1 si es que tenemos otras camaras'''
cap= cv2.VideoCapture(0)

#'''impportar las librerias entrenadas de ojos y cara'''
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eyes_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
#'''creacion del frame (ventana de video)'''
while True:
    ret, frame = cap.read()

 #   '''transformando a escala de grises'''
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    caras = face_cascade.detectMultiScale(gray,1.3,5)

    for (x,y,w,h) in caras:

  #   '''dibujando los rectangulos de deteccion de cara'''

     cv2.putText(frame,'Rostro',(x,y-20),2,0.5,(255,0,0),1,cv2.LINE_AA) 
     cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),5)  

     roi_gray = gray[y:y+w,x:x+w]
     roi_color = frame[y:y+h,x:x+w]

     ojos = eyes_cascade.detectMultiScale(roi_gray,1.3,5)

     for (ox,oy,ow,oh) in ojos:
        cv2.putText(frame,'Ojos',(x,y+60),2,0.8,(0,255,0),1,cv2.LINE_AA)
        cv2.rectangle(roi_color,(ox,oy),(ox+ow,oy+oh),(0,255,0),5)



    cv2.imshow('Deteccion facial y de ojos', frame)

    if (cv2.waitKey(1)==ord('q')):

      break
cap.release()
cv2.destroyAllWindows()