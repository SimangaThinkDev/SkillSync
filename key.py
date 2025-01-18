import pyrebase

fireBaseConfig = {
  "apiKey": "AIzaSyAzl1VAikvDeIZaOYcyJKHZl8axUrOhkhU",
  "authDomain": "fir-withpython-83ec8.firebaseapp.com",
  "databaseURL": "https://fir-withpython-83ec8-default-rtdb.firebaseio.com/",
  "projectId": "fir-withpython-83ec8",
  "storageBucket": "fir-withpython-83ec8.firebasestorage.app",
  "messagingSenderId": "433507983455",
  "appId": "1:433507983455:web:25f7c6a2f0027d598efbea"
}

# Initialize FireBase
firebase = pyrebase.initialize_app(fireBaseConfig)
