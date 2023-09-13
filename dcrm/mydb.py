import mysql.connector
# create db connection
dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Mysql#2121'
)
# prepare cursor obejct
cursorObject = dataBase.cursor()

# create a db
cursorObject.execute("CREATE DATABASE crmdb")
print("All done")