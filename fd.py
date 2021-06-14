import cv2
from random import randrange

trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# img = cv2.imread('fr.jpg')
# bwimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
webcam = cv2.VideoCapture(0)
while True:
    rdframe, frame = webcam.read()
    bwvid = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    face_crdnts = trained_face_data.detectMultiScale(bwvid)
    for i in range(len(face_crdnts)):
        (x, y, w, h) = face_crdnts[i]
        cv2.rectangle(frame, (x, y), (x + w, y + h), (randrange(269), randrange(269), randrange(269), 4))

    cv2.imshow("That's u!!", frame)
    cv2.waitKey(1)
    print("I am done!")

# face_crdnts = trained_face_data.detectMultiScale(bwwc)
# print(len(face_crdnts))

# for i in range(len(face_crdnts)):
#     (x, y, w, h) = face_crdnts[i]
#     cv2.rectangle(webcam, (x, y), (x + w, y + h), (randrange(269), randrange(269), randrange(269), 4))





