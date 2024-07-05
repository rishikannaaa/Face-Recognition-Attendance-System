import face_recognition
import cv2
import numpy as np
import csv
from datetime import datetime
import os
from mor3 import Database
import pyttsx3
import sys
import time
from mor3 import Database
db=Database()
text = pyttsx3.init()
voices=text.getProperty('voices')
text.setProperty('voice',voices[1].id)
text.setProperty('rate',130)

def audio(pl):    
    text.say(pl)
    text.runAndWait()
video_capture = cv2.VideoCapture(0)
photos=[]
path="C:\\Users\\okesh\\OneDrive\\Desktop\\FaceRecognition\\faces"
for photo in os.listdir(path):
    if (photo.endswith(".jpg") or photo.endswith(".jpeg")) or (photo.endswith(".png") or photo.endswith(".webp")) or (photo.endswith(".gif") or photo.endswith(".svg")) or (photo.endswith(".png") or photo.endswith(".avif")):
        photos.append(str(str(path)+"\\"+str(photo)))
known_face_encodings=[]
for path in photos:
    #print(path)
    known_face_encodings.append(face_recognition.face_encodings(face_recognition.load_image_file(path))[0])



##"""
##C:\Users\okesh\OneDrive\Desktop\FaceRecognition\faces\1004.jpg
##C:\Users\okesh\OneDrive\Desktop\FaceRecognition\faces\1005.jpg
##C:\Users\okesh\OneDrive\Desktop\FaceRecognition\faces\1006.jpg
##C:\Users\okesh\OneDrive\Desktop\FaceRecognition\faces\1011.jpg
##C:\Users\okesh\OneDrive\Desktop\FaceRecognition\faces\1012.jpg
##C:\Users\okesh\OneDrive\Desktop\FaceRecognition\faces\1014.jpg
##C:\Users\okesh\OneDrive\Desktop\FaceRecognition\faces\Rdj.jpg
##C:\Users\okesh\OneDrive\Desktop\FaceRecognition\faces\shahrukh.jpg
##C:\Users\okesh\OneDrive\Desktop\FaceRecognition\faces\tom.jpg
##
### Load known faces
##shahruhk_image = face_recognition.load_image_file("faces/shahrukh.jpg")
##shahruhk_encoding = face_recognition.face_encodings(shahruhk_image)[0]
##
##tom_image = face_recognition.load_image_file("faces/tom.jpg")
##tom_encoding = face_recognition.face_encodings(tom_image)[0]
##"""

#known_face_encodings = [shahruhk_encoding, tom_encoding, rdj_encoding]
known_face_names = ["1004","1005","1006","1011","1012","1014", "1015","rdj","tom"]


known_face_names = []
for path in photos:
    known_face_names.append(str(path)[54:].replace(".jpg","").replace(".jpeg","").replace(".png","").replace(".webp","").replace(".gif","").replace(".svg","").replace(".avif",""))

print(known_face_names)


#List of expected students
students = known_face_names.copy()

face_locations = []
face_encodings = []

#Get the current date and time

now = datetime.now()
current_date = now.strftime("%Y-%m-%d")

f = open(f"{current_date}.csv", "w+", newline="")
lnwriter = csv.writer(f)

while True:
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
            fontColor = (309, 0, 0)
            thickness = 3
            lineType = 2
            

            ret_val=db.attendance_insert(name)
            emp_name=db.find_name(str(name))
            
            if int(ret_val)==1:
                cv2.putText(frame, str(emp_name)+"-"+str(name)+"\nNow present", bottomLeftCornerOfText, font,fontScale,fontColor, thickness, lineType)
                audio("Welcome to MOR cube "+str(emp_name))
                time.sleep(10)
                
            elif int(ret_val)==0:
                cv2.putText(frame, str(emp_name)+"-"+str(name)+"\nNow Left", bottomLeftCornerOfText, font, fontScale,fontColor, thickness, lineType)
                audio("You are exited "+str(emp_name))
                time.sleep(10)
                
            else:
                cv2.putText(frame, str(emp_name)+"-"+str(name)+"\nAlready exited", bottomLeftCornerOfText, font, fontScale,fontColor, thickness, lineType)
                audio("Already exited"+str(emp_name))
                time.sleep(10)
            
        if name in students:
            students.remove(name)
            current_time = now.strftime("%H-%M%S")
            lnwriter.writerow([name, current_time])
            #sys.exit()

    cv2.imshow("attendace", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    time.sleep(1)
video_capture.release()
cv2.destroyAllWindows()
f.close()
