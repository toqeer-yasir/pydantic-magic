from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int

user = User(name="Toqeer", age=23)


data_dict = user.model_dump()
data_dict_name = user.model_dump(include=['name'])
data_dict_rather_name = user.model_dump(exclude=['name'])

print(f"{data_dict=}")
print(f"{data_dict_name=}")