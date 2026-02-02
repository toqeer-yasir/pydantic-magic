from pydantic import BaseModel, Field
from typing import List


class Student(BaseModel):
    name: str = Field(..., min_length=2, max_length=44)
    age: int = Field(..., ge=18, le=25)
    experience: int = Field(..., description='Enter experience in years.', gt=5, lt=15)
    grade: float = Field(..., ge=0.0, le=100.0)


def student_details(student: Student):
    print(f"{student.name=}")
    print(f"{student.experience=}")
    print(f"{student.age=}")
    print(f"{student.grade=}")


student1 = Student(name='Toqeer', experience=11, age=20, grade=77.2)

print('-'* 30)
student_details(student1)