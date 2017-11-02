"""
The class Timer from threading module represents an action that 
should take place after a specified amount of time.

We can cancel the Timer instance anytime in the running process, even before it started.
"""
import subprocess

from threading import Timer


kill = lambda process: process.kill()  # we set a lambda that can kill the process
cmd = ['ping', 'www.google.com']  # sets the command
ping = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# waits 5 seconds before calling kill with the argument ping
my_timer = Timer(5, kill, [ping]) 

try:
	my_timer.start()
	stdout, stderr = ping.communicate()
finally:
	my_timer.cancel()

print (str(stdout))
