from pydantic import BaseModel, Field, field_validator
from typing import List, Optional


class SaleMan(BaseModel):
    name: str = Field(..., min_length=2, max_length=20, examples=['Toqeer', 'Faizan', 'Abdullah'])
    f_name: str = Field(..., min_length=2, max_length=20, examples=['RAFIQUE'])
    service: int = Field(..., ge=3, le=10)

    @field_validator('name')# validate field or no. of fields (name, title, f_name) or all ('*').
    def name_should_be(cls, e: str) -> str: # cls makes this functin @classmethod and -> str return the string or return type of function.
        if ' ' in e:
            raise ValueError("name must be without spaces!")
        else:
            return e.lower()
        
    @field_validator('f_name')
    def name_should_be(cls, e: str) -> str:
        if not e.isupper():
            raise ValueError("f_name must be in ALL capital letters!")
        else:
            return e
        
    @field_validator('service')
    def name_should_be(cls, e: str) -> str: # to convert service in months.
        return e*12
        

saleman1 = SaleMan(name='Toqeer', f_name='YASIR', service=6)

print('-' * 30)
print(f"{saleman1.name=}")
print(f"{saleman1.f_name=}")
print(f"{saleman1.service=} months.")