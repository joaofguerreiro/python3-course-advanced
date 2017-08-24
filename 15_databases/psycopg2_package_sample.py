import psycopg2


conn = psycopg2.connect(dbname='my_database', user='username')
cursor = conn.cursor()

# execute a query
cursor.execute("SELECT * FROM table_name")
row = cursor.fetchone()

# close your cursor and connection
cursor.close()
conn.close()
# Traceback (most recent call last):
#   File "psycopg2_package_sample.py", line 4, in <module>
#     conn = psycopg2.connect(dbname='my_database', user='username')
#   File "/usr/local/lib/python3.6/site-packages/psycopg2/__init__.py", line 130, in connect
#     conn = _connect(dsn, connection_factory=connection_factory, **kwasync)
# psycopg2.OperationalError: could not connect to server: No such file or directory
# 	Is the server running locally and accepting
# 	connections on Unix domain socket "/tmp/.s.PGSQL.5432"?
