import cv2
import numpy as np
from os import makedirs
from os.path import isdir

f_dir = './faceimg/'
xml = './haarcascade_frontalface_default.xml'

f_classifier = cv2.CascadeClassifier(xml)

def f_find(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    f = f_classifier.detectMultiScale(gray, 1.3, 5)

    if f is():
        return None

    for (x,y,w,h) in f:
        cap_face = img[y:y+h, x:x+w]

    return cap_face

def f_save(dname):
    if not isdir(f_dir+dname):
        makedirs(f_dir+dname)

    cam = cv2.VideoCapture(0)
    count = 0

    while True:
        ret, frame = cam.read()

        if f_find(frame) is not None:
            count+=1

            face = cv2.resize(f_find(frame),(200,200))
            face =  cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

            f_name_path = f_dir + dname + '/' + dname + str(count)+'.jpg'
            cv2.imwrite(f_name_path, face)
            cv2.putText(face, str(count), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
            cv2.imshow('Face Cropper', face)
        else:
            print('Face Not Found')
            pass

        if cv2.waitKey(1) == 13 or count == 100:
            break
    cam.release()
    cv2.destroyAllWindows()

if __name__ == "__main__" :
    f_save('seoungha  c')