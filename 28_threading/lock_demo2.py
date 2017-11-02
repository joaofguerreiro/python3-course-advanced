import threading


total = 0
lock = threading.RLock()  # is the Re-Entrant Lock (self-explanatory name)


def do_something():

    with lock:
        print('Lock acquired in the do_something function')
    print('Lock released in the do_something function')

    return "Done doing something"


def do_something_else():
    with lock:
        print('Lock acquired in the do_something_else function')
    print('Lock released in the do_something_else function')

    return "Finished something else"


def main():
    with lock:  # acquires the lock
        result_one = do_something()
        result_two = do_something_else()

    print (result_one)
    print (result_two)


if __name__ == '__main__':
    for i in range(5):
        my_thread = threading.Thread(target=main)
        my_thread.start()
# Lock acquired in the do_something function
# Lock released in the do_something function
# Lock acquired in the do_something_else function
# Lock released in the do_something_else function
# Done doing something
# Lock acquired in the do_something function
# Finished something else
# Lock released in the do_something function
# Lock acquired in the do_something_else function
# Lock released in the do_something_else function
# Done doing something
# Finished something else
# Lock acquired in the do_something function
# Lock released in the do_something function
# Lock acquired in the do_something_else function
# Lock released in the do_something_else function
# Done doing something
# Finished something else
# Lock acquired in the do_something function
# Lock released in the do_something function
# Lock acquired in the do_something_else function
# Lock released in the do_something_else function
# Done doing something
# Finished something else
# Lock acquired in the do_something function
# Lock released in the do_something function
# Lock acquired in the do_something_else function
# Lock released in the do_something_else function
# Done doing something
# Finished something else
