import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="xyz",
  database="shobhit"
)

cursor = mydb.cursor()

#quary for creating table 

cursor.execute("CREATE TABLE user (username VARCHAR(100), password VARCHAR(100))")
cursor.execute("CREATE TABLE address (pincode INT(2O),state VARCHAR(100),country VARCHAR(100),phone_no INT(20))")


# for showing how many table in dtabase
cursor.execute("SHOW TABLES")
for x in cursor:
    print(x)


# for multiple address : using Foreign keys 
# syntax :
#  FOREIGN KEY (userID) REFERENCES user(user ID)  