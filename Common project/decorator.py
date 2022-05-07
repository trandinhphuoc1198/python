from functools import wraps

def timer(orig_func):
    import time
    @wraps(orig_func)
    def wrapper(*args,**kwargs):
        start = time.time()
        result= orig_func(*args,**kwargs)
        end = time.time()
        print(f'Function {orig_func.__name__} took {round(end-start,3)} seconds')
        return result
    return wrapper

def logging(orig_func):
    import logging
    logging.basicConfig(filename=f'{orig_func.__name__}.log',level=logging.INFO)
    @wraps(orig_func)
    def wrapper(*args,**kwargs):
        from datetime import datetime
        logging.info(f'{datetime.now()} : {orig_func.__name__} was run')
        return orig_func(*args,**kwargs)
    return wrapper
        

import time
# @logging
# @timer
def print_number(num):
    time.sleep(1)
    print(num)
print_number(4)