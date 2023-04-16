import os
import cv2
import pickle
import face_recognition

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL' : "https://faceauthenticator-570df-default-rtdb.firebaseio.com/",
    'storageBucket' : "faceauthenticator-570df.appspot.com"
})


# Importing student images into a list
imgFolderPath = 'images'
imgPathList = os.listdir(imgFolderPath)
print(imgPathList)
imgList = []
studentIds = []

for path in imgPathList:
    imgList.append(cv2.imread(os.path.join(imgFolderPath, path)))
    studentIds.append(os.path.splitext(path)[0])

    fileName = f'{imgFolderPath}/{path}'
    bucket = storage.bucket()
    blob = bucket.blob(fileName)
    blob.upload_from_filename(fileName)


def findEncodings(imagesList):
    encodeList = []
    for img in imagesList:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    
    return encodeList 

print("Encoding started...")
encodeListKnown = findEncodings(imgList)
encodeListKnownWithIds = [encodeListKnown, studentIds]
# print(encodeListKnown)
# print(studentIds)
print("Encoding completed")

file = open("EncodeFile.p",'wb')
pickle.dump(encodeListKnownWithIds, file)
file.close()
print("File saved...")