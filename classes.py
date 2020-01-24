class User:

    # Class 
    active_users = 0

    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        User.active_users += 1

    def logout(self):
        User.active_users -= 1
        return f"{self.first} has logged out."

    def full_name(self):
        return f"{self.first} {self.last}"

    def initials(self):
        return f"{self.first[0]}.{self.last[0]}."

    def likes(self, thing):
        return f"{self.first} likes {thing}."

    def ofAge(self):
        return self.age >= 21


class BankAccount:
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0.0
        
    def getBalance(self):
        return self.balance
        
    def deposit(self, amount):
        self.balance += amount
        return self.balance
        
    def withdraw(self, amount):
        self.balance -= amount
        return self.balance



user1 = User("Joe", "Blake", 33)
user2 = User("Juliana", "Crane", 31)
print(user2.full_name())
print(user1.initials())
print(user1.likes("cigarettes"))
print(User.active_users)
print(user2.logout())
print(User.active_users)

