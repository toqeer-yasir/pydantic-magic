from pydantic import BaseModel, computed_field

# we can compute a field that we don't need to take from user but can be calculated from the user inputs:
class Patient(BaseModel):
    name: str
    age: int
    weight: int
    height: float

    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight/(self.height**2), 2)
        return bmi
    

patient1 = Patient(name='UBL', age=45, weight=70, height=1.8)

print('-'* 30)
print(f"{patient1.name=}")
print(f"{patient1.age=}")
print(f"{patient1.bmi=}") # insted of bmi computed variable we need to pass bmi function.