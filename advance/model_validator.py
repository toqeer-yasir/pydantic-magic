from pydantic import BaseModel, model_validator, Field
from typing import Dict, List, Annotated, Literal


class Patient(BaseModel):
    name: str
    age: int= Field(..., ge=20, le=70, description="Patient age should be in years.")
    condition: Literal['normal', 'serious']
    details: Dict[str, str]

    @model_validator(mode='after')
    def check_contact(self):
        if self.age > 60 and 'contact' not in self.details:
            raise ValueError("Please add patient contact details.")
        else:
            return self
        
        
patient1 = Patient(name='UBL', age=61, condition='serious', details={'address': 'faislabad', 'status': 'mental', 'gender': 'male'})

print('-'* 30)
print(f"{patient1.name=}")
print(f"{patient1.age=}")
print(f"{patient1.condition=}")
print(f"{patient1.details=}")