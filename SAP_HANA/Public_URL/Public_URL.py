from hdbcli import dbapi
connection =dbapi.connect(address='linux-y87l', port=39013, user='system', password='Bharat@11')

print('Connected  to DB :' + str(connection.isconnected()))

try: 
    cursor = connection.cursor()
    cursor.execute("ALTER SYSTEM ALTER CONFIGURATION ('xsengine.ini', 'database', 'D21') SET ('public_urls', 'http_url') = 'http://linux-y87l:8090' WITH RECONFIGURE;")
    cursor.execute("ALTER SYSTEM ALTER CONFIGURATION ('xsengine.ini', 'database', 'D21') SET ('public_urls', 'https_url') = 'https://linux-y87l:4390' WITH RECONFIGURE;")
    
    print("Https Public Setting Configured..")
   
except:
    print("Error While Performing Operation...")
    
finally:
    cursor.close()
    print("Cursor Closed.")
    connection.close()
    print("DB Connection Disconnected.")      
    connection.close()