import sqlite3 as s
connection = s.connect("Hospital.db")

getdoctorid= input("Enter doctor ID to delete: ")

result = connection.execute("DELETE FROM doctor WHERE ID="+getdoctorid)
connection.commit()
print("Deleted Successfully")