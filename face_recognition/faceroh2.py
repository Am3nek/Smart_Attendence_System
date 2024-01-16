import cv2
import face_recognition
import os
import numpy as np
from datetime import datetime
import pickle
import requests
import json
import time
import threading

path = 'student_images'
images = []
classNames = []

glb_name=''
mylist = os.listdir(path)

for cl in mylist:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])

def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encoded_face = face_recognition.face_encodings(img)[0]
        encodeList.append(encoded_face)
    return encodeList
encoded_face_train = findEncodings(images)

def markAttendance(name):
    global glb_name
    if(name!=glb_name):
        url = 'http://127.0.0.1:8000/SData/data/'+name.upper()
        response = requests.get(url)

        if response.status_code == 200:
            print(response.json())
        else:
            print("Failed to get tasks.")
        glb_name=name
    else:
        print("Name already Attended")
    


cap  = cv2.VideoCapture("http://192.168.210.223:81/stream")
while True:
    success, img = cap.read()
    imgS = cv2.resize(img, (0,0), None, 0.25,0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
    faces_in_frame = face_recognition.face_locations(imgS)
    encoded_faces = face_recognition.face_encodings(imgS, faces_in_frame)
    for encode_face, faceloc in zip(encoded_faces,faces_in_frame):
        matches = face_recognition.compare_faces(encoded_face_train, encode_face)
        faceDist = face_recognition.face_distance(encoded_face_train, encode_face)
        matchIndex = np.argmin(faceDist)
        print(matchIndex)
        if matches[matchIndex]:
            name = classNames[matchIndex].upper().lower()
            markAttendance(name)
    cv2.imshow('webcam', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break