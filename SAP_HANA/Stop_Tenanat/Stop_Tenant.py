from hdbcli import dbapi
connection =dbapi.connect(address='linux-y87l', port=39013, user='system', password='Bharat@11')

print('Connected  to DB :' + str(connection.isconnected()))

try: 
    cursor = connection.cursor()
    cursor.execute("ALTER SYSTEM STOP DATABASE D21")
    print("Database Stopped..")
except:
    print("Error While Performing Operation...")
finally:
    cursor.close()
    print("Cursor Closed.")
    connection.close()
    print("DB Connection Disconnected.")      
    connection.close()