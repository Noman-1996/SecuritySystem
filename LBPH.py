import cv2
#import securityDashboard as sd
import os
import numpy as np
import errno
import tkinter
from tkinter import messagebox
#import GetAllStudent as gs
import queries as q
#import MainScreen as ms
import adminDashboard as ad
import sys
import threading

face_recognizer = None

# sus = ["scabbard", "assault_rifle", "rifle", "revolver", "hatchet", "knife", "holster", "bow", "cleaver"]
ar = []
vr = []


def close():
    sys.exit()

def thread(tup):
    messagebox.showinfo('Information', 'ID : ' + tup[0] + "\nName : " + tup[1] + "\nDegree : " + tup[
                        2] + "\nSemister : " + str(tup[3]) + "\nStatus : " + tup[4])
    

def click(event, x, y, flags, param):
    global ar, vr
    if event == cv2.EVENT_LBUTTONDOWN:
        print('call')
        for i in range(0, len(ar)):
            if ar[i][0] < x < ar[i][2] and ar[i][1] < y < ar[i][3]:
                if vr[i] != 'unknown':
                    tup = q.readData(vr[i])
                    print(tup)
                    print(vr[i])
                    # window = tkinter.Toplevel()
                    # window.resizable(False, False)

                    # window.geometry("350x350+500+150")
                    # window.title("Student Information")

                    # infolbl = tkinter.Label(window,
                    #             text= "ID : " + tup[0] + "\nName : " + tup[1] + "\nDegree : " + tup[
                    #                 2] + "\nSemister : " + str(tup[3]) + "\nStatus : " + tup[4],
                    #             bd=1,
                    #             relief ="solid",
                    #             font="Times 24",
                    #             width = 15,
                    #             height = 8)
                    # infolbl.pack()
                    
                    
                    # button = tkinter.Button(window,
                    #     text="OK",
                    #     fg="red",
                    #     width=27,
                    #     command=close
                    #     )
                    # button.place(x=70, y=250)

                    x = threading.Thread(target=thread, args=(tup,))
                    x.start()
                    # messagebox.showinfo('Information', 'ID : ' + tup[0] + "\nName : " + tup[1] + "\nDegree : " + tup[
                    #     2] + "\nSemister : " + str(tup[3]) + "\nStatus : " + tup[4])




def detect_face(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    face_cascade = cv2.CascadeClassifier('opencv-files/haarcascade_frontalface_alt.xml')

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5);

    if len(faces) == 0:
        return None, None

    (x, y, w, h) = faces[0]

    return gray[y:y + w, x:x + h], faces[0]


def detect_face2(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    face_cascade = cv2.CascadeClassifier('opencv-files/haarcascade_frontalface_alt.xml')

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5);
    print(faces)
    if len(faces) == 0:
        return None, None

    return gray, faces

#function for loading training data
def prepare_training_data(data_folder_path):
    dirs = os.listdir(data_folder_path)

    i = 0

    faces = []

    labels = []

    for dir_name in dirs:

        label = int(dir_name)

        subject_dir_path = data_folder_path + "/" + dir_name

        subject_images_names = os.listdir(subject_dir_path)

        for image_name in subject_images_names:

            i += 1

            if image_name.startswith("."):
                continue;

            image_path = subject_dir_path + "/" + image_name

            image = cv2.imread(image_path)

            face, rect = detect_face(image)

            if face is not None:
                faces.append(face)

                labels.append(label)

    return faces, labels


def make_sure_path_exists(filePath):
    exists = os.path.isfile(filePath)
    if exists:
        # Store configuration file values
        return False
    else:
        os.makedirs(filePath)
        return True

def Training():
    face_recognizer = cv2.face.LBPHFaceRecognizer_create()

    faces, labels = prepare_training_data("TrainingData")

    face_recognizer.train(faces, np.array(labels))

    face_recognizer.save("opencv-files/lbphModelKnowledge.xml")

    messagebox.showinfo('Success', "Training Compelete")


#Model loading function
def realTimeLbph():
    global face_recognizer

    if os.path.isfile("opencv-files/lbphModelKnowledge.xml"):

        face_recognizer = cv2.face.LBPHFaceRecognizer_create()

        face_recognizer.read("opencv-files/lbphModelKnowledge.xml")

        return "ok"

    else:
        return "Error"


def predict(test_img):
    global face_recognizer, ar, vr

    ar.clear()

    vr.clear()

    img = test_img

    imgs, pos = detect_face2(img)

    if pos is not None:

        for p in pos:

            (x, y, w, h) = p

            label, confidence = face_recognizer.predict(imgs[y:y + w, x:x + h])
            print(confidence)
            if confidence < 60:

                label_text = str(label)

            else:

                label_text = 'unknown'

            (x, y, w, h) = p

            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            ar.append((x, y, x + w, y + h))

            cv2.putText(img, label_text, (x + 50, y - 20), cv2.FONT_HERSHEY_PLAIN, 2.5, (0, 255, 0), 2)
            vr.append(label_text)

        return img

    return test_img


def trainStudent(studname):
    
    startTraining = True    
    i = 0
    if startTraining:
        st = cv2.VideoCapture(0)    

        if st.isOpened():
            while True:
                ret, original = st.read()

                cv2.imshow("Training", original)

                cv2.imwrite("TrainingData/" + studname + "/" + str(i) + ".jpg", original)

                i += 1

                if cv2.waitKey(1) & 0xFF == ord('q'):                        
                        st.release()
                        cv2.destroyAllWindows()
                        break
                        # Training()
                        #ms.calls()                   
                                              

                # if cv2.getWindowProperty(ty, cv2.WND_PROP_VISIBLE) < 1:
                #     break

            st.release()
            cv2.destroyAllWindows()
            Training()
            ad.loadAdminForm()

def prediction(ipvalue):
    if realTimeLbph() == "ok":
        pred = cv2.VideoCapture(ipvalue)

        if pred.isOpened():
            while True:
                ret, original = pred.read()

                cv2.imshow("Prediction", predict(original))                  
                cv2.setMouseCallback("Prediction", click)

                reimage = np.array(cv2.resize(original, (224, 224)))

                image = reimage.reshape(
                    (1, reimage.shape[0], reimage.shape[1], reimage.shape[2])).astype(float)
                if cv2.waitKey(1) & 0xFF == ord('q'):                        
                        pred.release()
                        cv2.destroyAllWindows()
                        #sd.load()
                        break
            pred.release()
            cv2.destroyAllWindows()
    else:
        messagebox.showerror("Error", "Model Not Found")

