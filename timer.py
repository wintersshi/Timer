import time
from time import strftime
from contextlib import contextmanager

@contextmanager
def timer(message):
    """ Time counting
    """
    print('[{}][{}] Begin ...'.format(strftime('%Y-%m-%d %H:%M:%S'), message))
    t0 = time.time()
    yield
    print('[{}][{}] End   ...'.format(strftime('%Y-%m-%d %H:%M:%S'), message))
    print('[{}][{}] Cost {:.2f} s'.format(strftime('%Y-%m-%d %H:%M:%S'), message, time.time() - t0))

