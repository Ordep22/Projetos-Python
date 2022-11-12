import cv2
from tracker import *
##Abre o vídeos para inciar a detecção freme após frame
tracker = EuclideanDistTracker()
cap  = cv2.VideoCapture("/Users/PedroVitorPereira/PycharmProjects/CursodePython/TCC-1/Vídeos Resende - Bobinas CG/c-00-20200819-194148.ts")
##Detecção de através do Stable Camera
object_detector  = cv2.createBackgroundSubtractorMOG2(history =  500 , varThreshold =  16 , detectShadows =  True)
while True:
    ret, frame  = cap.read()
##Seleção da área de interesse
    roi = frame[0:680,0:720]
##1_Detecção de obejtos
    mask = object_detector.apply(roi)
    _, mask = cv2.threshold(mask, 254, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    detections = []
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 8000 and area < 13000:
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(roi, (x,y),(x+w, y+w),(0,255,0),3)
            detections.append([x,y,w,h])
##2_Seguindo do objeto

    boxes_ids = tracker.update(detections)

    for box_ids in boxes_ids:
        x,y,w,h,id = box_ids
        cv2.putText(roi, str(id),(x,y - 15),cv2.FONT_HERSHEY_PLAIN,3,(255,0,0),2)
        cv2.rectangle(roi, (x,y),(x+w, y+w),(0,255,0),3)
    cv2.imshow("Frame",frame)
    cv2.imshow("Mask",mask)
    cv2.imshow("roi",roi)
    key = cv2.waitKey(1)

    if key == 27:
        break

cap.read()
cv2.destroyAllWindows()




