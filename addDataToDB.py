import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL':"https://faceauthenticator-570df-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "101" : {
        "name" : "A R Kaarthikeyan",
        "major" : "CSE",
        "starting_year" : 2020,
        "total_attendance" : 5,
        "year" : 3,
        "standing" : "G",
        "last_attendance_time": "2023-03-28 12:30:58"
    },
    "102" : {
        "name" : "Elon Musk",
        "major" : "CSE",
        "starting_year" : 2020,
        "total_attendance" : 4,
        "year" : 3,
        "standing" : "G",
        "last_attendance_time": "2023-03-28 12:30:58"
    },
    "103" : {
        "name" : "Ratan Tata",
        "major" : "Economics",
        "starting_year" : 2020,
        "total_attendance" : 8,
        "year" : 4,
        "standing" : "G",
        "last_attendance_time": "2023-03-28 12:30:58"
    },
    "104" : {
        "name" : "Steve Jobs",
        "major" : "IT",
        "starting_year" : 2020,
        "total_attendance" : 3,
        "year" : 3,
        "standing" : "G",
        "last_attendance_time": "2023-03-28 12:30:58"
    },
    
}

for key,value in data.items():
    ref.child(key).set(value)