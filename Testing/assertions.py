def add_positive_numbers(x, y):
    assert x > 0 and y > 0, "Both numbers must be positive!"
    return x + y


print(add_positive_numbers(1,2)) #3
# print(add_positive_numbers(1,-3)) #Assertion Error


def eat_junk(food):
    assert food in ["pizza", "ice cream", "candy", "fried butter"], "Food must be in 'junk food' list"
    return f"nom nom nom, I'm eating {food}!"

food = input("Please enter the food you're eating: ").lower()
print(eat_junk(food))

