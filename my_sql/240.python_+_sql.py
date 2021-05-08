#status
#pip install mysql-connector-python

import mysql.connector

conn = mysql.connector.connect(host='localhost', username='root')
print(conn)