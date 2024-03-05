import mysql.connector
class user_model():
    def __init__(self):
        # connection establishment code
        try:
            mysql.connector.connect(host="localhost",user="root",password="",database="restAPI")
            print("Connection Sucessful")
        except Exception as e:
            print("The error is: ",e)
    def user_signup_model(self):
        return "This is user_signup"