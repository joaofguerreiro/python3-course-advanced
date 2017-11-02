import logging
import threading


def get_logger():
    """
    This piece of code will create a logger that’s set to the debug level. 
    It will save the log to the current working directory (i.e. where the script is run from) 
    and then we set up the format for each line logged. 
    The format includes the time stamp, the thread name, the logging level and the message logged.
    """
    logger = logging.getLogger("threading_example")
    logger.setLevel(logging.DEBUG)

    fh = logging.FileHandler("threading.log")
    fmt = '%(asctime)s - %(threadName)s - %(levelname)s - %(message)s'
    formatter = logging.Formatter(fmt)
    fh.setFormatter(formatter)

    logger.addHandler(fh)
    return logger


def doubler(number, logger):  # we pass the logger to the function so we have only one logging object during runtime
    """
    A function that can be used by a thread
    """
    logger.debug('doubler function executing')  # instead of printing, we log the statements
    result = number * 2
    logger.debug('doubler function ended with: {}'.format(result))


if __name__ == '__main__':
    logger = get_logger()
    thread_names = ['Mike', 'George', 'Wanda', 'Dingbat', 'Nina']
    for i in range(5):
        my_thread = threading.Thread(
            target=doubler, name=thread_names[i], args=(i,logger))
        my_thread.start() 
