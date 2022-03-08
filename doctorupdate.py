import sqlite3 as s

connection = s.connect("Hospital.db")

getPhone = input("Enter Phone Number: ")


getNewdname = input("Enter New Doctor Name: ")
getNewquali = input("Enter New Qualification: ")
getNewaddress = input("Enter New Address: ")
getNewphoneno = input("Enter New Phone Number: ")
getNewemail = input("Enter New Email: ")


result = connection.execute(" UPDATE DOCTOR SET DOCTOR_NAME='"+getNewdname+"', QUALIFICATION='"+getNewquali+"', \
ADDRESS='"+getNewaddress+"', PHONE_NUMBER="+getNewphoneno+", EMAIL='"+getNewemail+"' WHERE PHONE_NUMBER="+getPhone)
connection.commit()
print("Updated Successfully")