from pydantic import BaseModel

# defining a model:
class Patient(BaseModel):
    name: str
    age: int
    bed_no: int
    contact: int


# function that will use model:
def patient_entry(patient: Patient):
    print(f"{patient.name=}")
    print(f"{patient.age=}")
    print(f"{patient.bed_no=}")
    print(f"{patient.contact=}")


# object of the patient class(model):
patient1 = Patient(name='Hamza', age=22, bed_no=2434, contact=92312345679)

# use case:
print('-'*30)
patient_entry(patient1)