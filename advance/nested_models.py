from pydantic import BaseModel
from typing import List, Optional


class College(BaseModel):
    name: str
    location: str


class Education(BaseModel):
    graduated: bool
    phd_holder: bool


class Professor(BaseModel):
    name: str
    age: int
    college_info: College
    education_info: Education


professor1 = Professor(name='Toqeer', age=22, college_info={'name': 'Islamia_clg', 'location': 'fsd near new civil line'}, education_info={'graduated': 'yes', 'phd_holder': 'no'})

print('-'* 30)
print(f"{professor1.name=}")
print(f"{professor1.age=}")
print(f"{professor1.college_info=}")
print(f"{professor1.education_info=}")