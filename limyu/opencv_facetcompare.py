import cv2
import numpy as np
from os import listdir
from os.path import isdir, isfile, join

f_dir = './faceimg/'
xml = './haarcascade_frontalface_default.xml'

f_classifier = cv2.CascadeClassifier(xml)

def f_learning(dname):
    f_path = f_dir + dname + '/'
    f_pics = [f for f in listdir(f_path) if isfile(join(f_path, f))]

    Learning_data, Labels = [] , []

    for i , files in enumerate(f_pics):
        img_path = f_path + f_pics[i]
        imgs = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

        if imgs is None:
            continue

        Learning_data.append(np.array(imgs, dtype=np.uint8))
        Labels.append(i)
    if len(Labels) == 0:
        print("Learning Fail")
        return None

    Labels = np.asarray(Labels, dtype=np.int32)

    model = cv2.face.LBPHFaceRecognizer_create()
    model.train(np.asarray(Learning_data), np.asarray(Labels))
    print(model)
    return model

def learning_array():
    img_dirs = [f for f in listdir(f_dir) if isdir(join(f_dir,f))]
    models = {}
    for model in img_dirs:
        result = f_learning(model)
        if result is None:
            continue
        models[model] = result
    return models

def f_find(img, size=0.5):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = f_classifier.detectMultiScale(gray, 1.3, 5)
    if faces is():
        return img, []

    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255, 255), 2)
        roi = img[y:y+h, x:x+w]
        roi = cv2.resize(roi, (200,200))

    return img, roi

def execute(models):
    cam = cv2.VideoCapture(0)

    while True:
        ret, frame = cam.read()
        image, face = f_find(frame)

        try:
            min_score = 999
            min_score_name = ""

            face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

            for key, model in models.items():
                result = model.predict(face)
                if min_score > result[1] :
                    min_score = result[1]
                    min_score_name = key

            if min_score < 500 :
                confidence = int(100*(1-(min_score)/300))
                display_string = str(confidence) + '% Confidence is is '+ min_score_name
            cv2.putText(image,display_string,(100,120), cv2.FONT_HERSHEY_COMPLEX,1,(250,120,255),2)

            if confidence > 75 :
                cv2.putText(image, "Unlocked : " + min_score_name, (250,450), cv2.FONT_HERSHEY_COMPLEX, 1,(0,255,0), 2)
                cv2.imshow('Face Cropper' , image)
            else :
                cv2.putText(image, "Locked", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
                cv2.imshow('Face Cropper', image)
        except:
            cv2.putText(image, "Face Not Found", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
            cv2.imshow('Face Cropper', image)
            pass

        if cv2.waitKey(1) == 13:
            break
    cam.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    models = learning_array()
    execute(models)
