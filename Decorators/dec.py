# def be_polite(fn):
#     def wrapper():
#         print("What a pleasure to meet you!")
#         fn()
#         print("Have a great day!")
#     return wrapper

# def greet():
#     print("Hello my name is Jei.")

# def rage():
#     print("I hate you!")

# we are decorating our function
# with politeness

# greet =  be_polite(greet)
# greet()
# greet()
# greet()
# polite_rage = be_polite(rage)
# polite_rage()



def be_polite(fn):
    def wrapper():
        print("What a pleasure to meet you!")
        fn()
        print("Have a great day!")
    return wrapper

@be_polite
def greet():
    print("Hello my name is Jei.")

@be_polite
def rage():
    print("I hate you!")

greet()
rage()