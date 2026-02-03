from pydantic import BaseModel, Field
from typing import Annotated, List


# annotated is used with field to attach extra data or to bound data with variable:
class Rider(BaseModel):
    name: Annotated[str, Field(..., description='Name should be in capital letters.'), 'Example_name = Toqeer.']
    top_speed: Annotated[int, Field(..., ge=50, le=100, description="How fast rider can drive.")]
    bikes: Annotated[List[str], Field(..., description="How many types of bikes rider can control or drive.", min_length=2, max_length=10)]



rider1 = Rider(name='Toqeer', top_speed=90, bikes=['cd_70', 'cd_125', 'cd_150'])

print('-'* 30)
print(f"{rider1.name=}")
print(f"{rider1.top_speed=}")
print(f"{rider1.bikes=}")