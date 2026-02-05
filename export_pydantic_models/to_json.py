from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int
    contact: str
    height: float

user = User(name="Faizan", age=22, contact='+923001234567', height=1.82)


# to formated pretty json:
pretty_json = user.model_dump_json(indent=4)

# if we wanan only include one or specific no. of variables:
pretty_json_name = user.model_dump_json(indent=4, include=['name'])

# if we wanan exclude only one or specific no. of variables:
pretty_json_rather_name = user.model_dump_json(indent=4, exclude=['name'])


print(pretty_json)
print(pretty_json_name)
print(pretty_json_rather_name)