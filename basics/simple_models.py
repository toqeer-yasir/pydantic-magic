from pydantic import BaseModel


# first we define a model(class):
class User(BaseModel):
    name: str
    age: int


# how to use it:

# take input from the user1:
print('-'* 30)
name = input("Input name: ")
age = input("Input age: ")

user1 = User(name=name, age=age)

print()
print(f"{user1.name=}")
print(f"{user1.age=}")

# take input from the user2:
print('-'* 30)
name = input("Input name: ")
age = input("Input age: ")

user2 = User(name=name, age=age)

print()
print(f"{user2.name=}")
print(f"{user2.age=}")