from ftplib import FTP
import ftplib
import os
"""
If the FTP server that you’re connecting to requires TLS security, 
then you will want to import the FTP_TLS class instead of the FTP class. 
The FTP_TLS class supports a keyfile and a certfile.
"""


# =================== CONNECTING TO FTP SERVERS ===================
ftp = FTP('ftp.debian.org')
print (ftp.login())
# 230 Login successful.

ftp = FTP('ftp.cse.buffalo.edu')
print (ftp.login())
# 230 Guest login ok, access restrictions apply.


# # =================== NAVIGATING DIRECTORIES ===================
# # We called LIST which retrieves a list of files and/or folders 
# # along with their respective informations and prints them out.
# ftp.retrlines('LIST')  # The retrlines method prints out the result of the command we called.
# # total 28
# # drwxrwxrwx   2 0       0     4096 Sep  6  2015 .snapshot
# # drwxr-xr-x   2 202019  5564  4096 Sep  6  2015 CSE421
# # drwxr-xr-x   2 0       0     4096 Jul 23  2008 bin
# # drwxr-xr-x   2 0       0     4096 Mar 15  2007 etc
# # drwxr-xr-x   6 89987   546   4096 Sep  6  2015 mirror
# # drwxrwxr-x   7 6980    546   4096 Jul  3  2014 pub
# # drwxr-xr-x  26 0       11    4096 Apr 29  2016 users

# print (ftp.cwd('mirror'))  # cwd command to change our working directory to a different folder.
# # 250 CWD command successful.

# ftp.retrlines('LIST')  # The retrlines method prints out the result of the command we called.
# # total 16
# # drwxr-xr-x  3 89987  546  4096 Sep  6  2015 BSD
# # drwxr-xr-x  5 89987  546  4096 Sep  6  2015 Linux
# # drwxr-xr-x  4 89987  546  4096 Sep  6  2015 Network
# # drwxr-xr-x  4 89987  546  4096 Sep  6  2015 X11


# # =================== DOWNLOADING VIA FTP ===================
# ftp = FTP('ftp.debian.org')
# print (ftp.login())
# # 230 Login successful.

# print (ftp.cwd('debian'))
# # 250 Directory successfully changed.

# out = 'README'
# with open(out, 'wb') as f:  # We create the name of the file we want to save to and open it in write-binary mode.
# 	# We use the ftp object’s retrbinary to call RETR to retrieve the file and write it to our local disk.
# 	ftp.retrbinary('RETR ' + 'README.html', f.write)

# filenames = ftp.nlst()  # We call nlst which gives us a list of filenames and directories.
# print (filenames)
# # ['README', 'README.CD-manufacture', 'README.html', 'README.mirrors.html', 'README.mirrors.txt', 
# # 'dists', 'doc', 'extrafiles', 'indices', 'ls-lR.gz', 'pool', 'project', 'tools', 'zzz-dists']

# for filename in filenames:
# 	host_file = os.path.join('ftp_test', filename)
# 	try:
# 		with open(host_file, 'wb') as local_file:
# 			ftp.retrbinary('RETR ' + filename, local_file.write)
# 			# 			Traceback (most recent call last):
# 			#   File "ftplib_sample.py", line 66, in <module>
# 			#     with open(host_file, 'wb') as local_file:
# 			# FileNotFoundError: [Errno 2] No such file or directory: 'ftp_test/README'
# 	except ftplib.error_perm:
# 		pass
# ftp.quit()


# =================== UPLOADING TO FTP SERVER ===================
def ftp_upload(ftp_obj, path, ftype='TXT'):
	"""
	A function for uploading files to an FTP server
	@param ftp_obj: The file transfer protocol object
	@param path: The path to the file to upload
	"""
	if ftype == 'TXT':
		with open(os.path.expanduser(path)) as fobj:
			ftp.storlines('STOR ' + path, fobj)
	else:
		with open(os.path.expanduser(path), 'rb') as fobj:
			ftp.storbinary('STOR ' + path, fobj, 1024)

if __name__ == '__main__':
	ftp = FTP('ftp.debian.org')
	ftp.login()

	path = '~/Downloads/340944751-Yellowjackets-Freda-pdf.pdf'
	ftp_upload(ftp, path, ftype='PDF')

	ftp.quit()
# We don't have access to upload to the chosen FTP server, hence the following error.
# ftplib.error_perm: 550 Permission denied.
