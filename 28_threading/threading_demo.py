import threading
"""
Python has the Global Interpreter Lock (GIL) that basically makes all threads run inside of one master thread.
"""

def doubler(number):
    """
    A function that can be used by a thread
    """
    print (threading.currentThread().getName() + '\n')
    print (number * 2)


if __name__ == '__main__':
    for i in range(5):
        my_thread = threading.Thread(target=doubler, args=(i,))
        my_thread.start()
# Thread-1

# 0
# Thread-2

# Thread-3

# 4
# 2
# Thread-4

# Thread-5

# 6
# 8
