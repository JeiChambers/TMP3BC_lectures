from random import choice

def sum(n, func):
    total = 0 
    for num in range(n):
        total += func(num)
    return total

def square(x):
    return x*x

def cube(x):
    return x*x*x

print(sum(7, square))



# We can nest functions inside one another
def greet(person):
    def get_mood():
        msg = choice(('Hello there ', 'I love you ', 'Get lost '))
        return msg
    
    result = get_mood() + person
    return result

print(greet("Toby!"))
print(greet("Toby!"))
print(greet("Toby!"))



def make_laugh_at(person):
    def get_laugh():
        lol = choice(('Hahaha', 'LoL', 'Teheehee'))
        #Internal func using person variable from internal func #closure
        return f"{lol} {person}"

    return get_laugh

laugh_at = make_laugh_at("Linda!")

print(laugh_at())
print(laugh_at())
print(laugh_at())
    
    