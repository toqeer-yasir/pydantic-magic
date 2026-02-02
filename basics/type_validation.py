from pydantic import BaseModel, EmailStr, HttpUrl
from typing import List, Optional, Dict


# model: 
class Product(BaseModel):
    name: str
    price: int
    in_stoc: bool = True
    tags: List[str] = []
    address: Optional[Dict[str, str]] = {None, None}
    url: Optional[HttpUrl] = None
    email: Optional[EmailStr] = None


# function that will use pydantic model:
def product_details(product: Product):
    print(f"{product.name=}")
    print(f"{product.price=}")
    print(f"{product.in_stoc=}")
    print(f"{product.tags=}") # all the tags shuld be string
    print(f"{product.address=}")
    print(f"{product.url=}")
    print(f"{product.email=}") # shows error when we provide wrong email structure and it is optional
 

# object
product1 = Product(name='Detol', price=244, in_stoc=True, tags=['germs_protector', 'detol', 'skin_care', 'anti_infectant'], address={'temp': 'fsd', 'perm': 'shahkot'})

product2 = Product(name='Soap', price=299, in_stoc=False, tags=['germs_protector', 'Soap', 'skin_care', 'anti_infectant'], email='luxSoap@gmail.com', url="https://youtube.com.pk")

print('-'* 30)
product_details(product1)
print('-'* 30)
product_details(product2)
