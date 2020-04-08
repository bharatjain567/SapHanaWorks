from hdbcli import dbapi
connection =dbapi.connect(address='linux-y87l', port=39013, user='system', password='Bharat@11')

print('Connected  to DB :' + str(connection.isconnected()))

try: 
    cursor = connection.cursor()
    cursor.execute("Alter SYSTEM ALTER CONFIGURATION ('nameserver.ini','SYSTEM') set ('password policy','password_layout')='E8s*' with reconfigure;")
    cursor.execute("Alter SYSTEM ALTER CONFIGURATION ('nameserver.ini','SYSTEM') set ('minimal_password_length','password_layout')='8' with reconfigure;")
    print("Password Policy Updated..")
except:
    print("Error While Performing Operation")
finally:
    cursor.close()
    print("Cursor Closed.")
    connection.close()
    print("DB Connection Disconnected.")      





