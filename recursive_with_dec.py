import datetime
import time
def my_decorator(func):
    def wrapper (*args, **kwargs):
        print(f'This is the start time {datetime.datetime.now()}')
        n = func(*args)
        time.sleep(2)
        print(f'This is the end time {datetime.datetime.now()}')
        return n

    return wrapper

@my_decorator
def recursive(n):
    if n < 1:
        return 1
    else:
        number = n * recursive(n-1)
        return number

print(recursive(5))