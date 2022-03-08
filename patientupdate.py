import sqlite3 as s

connection = s.connect("Hospital.db")

getPatientid = input("Enter Patient ID to change: ")

getNewpid = input("Enter New Patient ID: ")
getNewpname = input("Enter New Patient Name: ")
getNewaddress = input("Enter New Address: ")
getNewphoneno = input("Enter New Phone Number: ")
getNewemail = input("Enter New Email: ")
getNewpincode = input("Enter New Pincode: ")

result = connection.execute(" UPDATE PATIENT SET PATIENT_ID="+getNewpid+", PATIENT_NAME='"+getNewpname+"', \
ADDRESS='"+getNewaddress+"', PHONE_NUMBER="+getNewphoneno+", EMAIL='"+getNewemail+"', PINCODE="+getNewpincode+" WHERE PATIENT_ID="+getPatientid)
connection.commit()
print("Updated Successfully")