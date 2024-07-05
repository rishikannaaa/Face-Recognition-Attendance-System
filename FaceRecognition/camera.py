import face_recognition
import cv2
import numpy as np
import csv
from datetime import datetime
import os
from mor3 import Database
import pyttsx3





text = pyttsx3.init()
voices=text.getProperty('voices')
text.setProperty('voice',voices[1].id)
text.setProperty('rate',200)

def audio(pl):    
    text.say(pl)
    text.runAndWait()




video_capture = cv2.VideoCapture(0)

photos=[]
path="C:\\Users\\okesh\\OneDrive\\Desktop\\FaceRecognition\\faces"













files_=os.listdir(path)
for photo in files_:
    if (photo.endswith(".jpg") or photo.endswith(".jpeg")) or (photo.endswith(".png") or photo.endswith(".webp")) or (photo.endswith(".gif") or photo.endswith(".svg")) or (photo.endswith(".png") or photo.endswith(".avif")):
        photos.append(str(str(path)+"\\"+str(photo)))

for photo in photos:
    print(photo)

# Load known faces
i=0
image=[]
encoding=[]
for photo in photos:
    
    image.append(face_recognition.load_image_file(photo))
    encoding.append(face_recognition.face_encodings(image[i])[0])

    i+=1

"""
    tom_image = face_recognition.load_image_file("faces/tom.jpg")
    tom_encoding = face_recognition.face_encodings(tom_image)[0]

    rdj_image = face_recognition.load_image_file("faces/Rdj.jpg")
    rdj_encoding = face_recognition.face_encodings(rdj_image)[0]
"""
known_face_encodings = encoding
known_face_names = photos

#List of expected students
#students = known_face_names.copy()

face_locations = []
face_encodings = []

#Get the current date and time
##
##now = datetime.now()
##current_date = now.strftime("%Y-%m-%d")

##f = open(f"{current_date}.csv", "w+", newline="")
##lnwriter = csv.writer(f)



db=Database()


hello=True
while hello:
    _, frame = video_capture.read()
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_RGB2HLS)

    #Recognize faces
    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    for face_encodings in face_encodings:
        matches = face_recognition.compare_faces(known_face_encodings, face_encodings)
        face_distance = face_recognition.face_distance(known_face_encodings, face_encodings)
        best_match_index = np.argmin(face_distance)

        name =""

        if(matches[best_match_index]):
            name = known_face_names[best_match_index]

#Add the text if a person is present
        if name in known_face_names:
            font = cv2.FONT_HERSHEY_SIMPLEX
            bottomLeftCornerOfText = (10, 100)
            fontScale = 1.5
            fontColor = (255, 0, 0)
            thickness = 3
            lineType = 2
            cv2.putText(frame, str(name)[54:], bottomLeftCornerOfText, font, fontScale, fontColor, thickness, lineType)


            name=str(name[54:]).replace(".jpg","")
            name=name.replace(".jpeg","")
            name=name.replace(".png","")
            name=name.replace(".webp","")
            name=name.replace(".gif","")
            name=name.replace(".svg","")
            name=name.replace(".avif","")

            #db.drop_create()
            #print(db.employee_add("okesh","admin"))
            ret_val=db.attendance_insert(int(name))
            emp_name=db.find_name(str(name))
            if int(ret_val)==1:
                audio("Welcome to MOR cube "+str(emp_name))
            elif int(ret_val)==0:
                audio("You are exited "+str(emp_name))
             #print(db.employee_status(12))
            #db.employee_disable(1001)
            data=db.employee_fetch()
            print(data["sno"])
            print(data["id"])
            print(data["name"])
            print(data["position"])
            print(data["in"])
            print(data["out"])
            print(data["status"])
            hello=False

##        if name in students:
##            students.remove(name)
##            current_time = now.strftime("%H-%M%S")
##            lnwriter.writerow([name, current_time])

    cv2.imshow("attendace", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


video_capture.release()
cv2.destroyAllWindows() 
