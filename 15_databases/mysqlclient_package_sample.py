import MySQLdb


conn = MySQLdb.connect('localhost', 'root', 'root', 'table_name')
cursor = conn.cursor()

cursor.execute("SELECT * FROM table_name")

# get a single row
row = cursor.fetchone()
print (row)


# disconnect from the database
conn.close()
# Traceback (most recent call last):
#   File "mysqlclient_package_sample.py", line 4, in <module>
#     conn = MySQLdb.connect('localhost', 'root', 'root', 'table_name')
#   File "/usr/local/lib/python3.6/site-packages/MySQLdb/__init__.py", line 86, in Connect
#     return Connection(*args, **kwargs)
#   File "/usr/local/lib/python3.6/site-packages/MySQLdb/connections.py", line 204, in __init__
#     super(Connection, self).__init__(*args, **kwargs2)
# _mysql_exceptions.OperationalError: (1049, "Unknown database 'table_name'")