def shout(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs).upper()
    return wrapper

@shout
def greet(name):
    return f"Hi, I'm {name}."

@shout
def order(main, side):
    return f"Hi, I'd like a {main}, with a side of {side}, please."

print(greet("Todd"))
print(order('burger', 'fries'))
print(order('quesadilla', 'churros'))