import time
from functools import wraps

def enforce(*types):
    def decorator(f):
        def new_func(*args, **kwargs):
            #convert args into something mutable
            newargs = []
            for (a, t) in zip(args, types):
                newargs.append( t(a))
            return f(*newargs, **kwargs)
        return new_func
    return decorator 

@enforce(str, int)
def repeat_msg(msg, times):
    for time in range(times):
        print(msg)

repeat_msg("hello", '3')


# Exercise Solution
# def delay(timer):
#     def inner(fn):
#         @wraps(fn)
#         def wrapper(*args, **kwargs):
#             print("Waiting {}s before running say_hi".format(timer, fn.__name__))
#             sleep(timer)
#             return fn(*args, **kwargs)
#         return wrapper
#     return inner