import pypyodbc


driver = 'DRIVER={SQL Server}'
server = 'SERVER=localhost'
port = 'PORT=1433'
db = 'DATABASE=testdb'
user = 'UID=me'
pw = 'PWD=pass'
conn_str = ';'.join([driver, server, port, db, user, pw])

conn = pypyodbc.connect(conn_str)
cursor = conn.cursor()

cursor.execute('select * from table_name')
row = cursor.fetchone()
rest_of_rows = cursor.fetchall()
# Traceback (most recent call last):
#   File "pyodbc_package_sample.py", line 12, in <module>
#     conn = pypyodbc.connect(conn_str)
#   File "/usr/local/lib/python3.6/site-packages/pypyodbc.py", line 2454, in __init__
#     self.connect(connectString, autocommit, ansi, timeout, unicode_results, readonly)
#   File "/usr/local/lib/python3.6/site-packages/pypyodbc.py", line 2507, in connect
#     check_success(self, ret)
#   File "/usr/local/lib/python3.6/site-packages/pypyodbc.py", line 1009, in check_success
#     ctrl_err(SQL_HANDLE_DBC, ODBC_obj.dbc_h, ret, ODBC_obj.ansi)
#   File "/usr/local/lib/python3.6/site-packages/pypyodbc.py", line 999, in ctrl_err
#     raise ProgrammingError('', 'SQL_ERROR')
# pypyodbc.ProgrammingError: ('', 'SQL_ERROR')
