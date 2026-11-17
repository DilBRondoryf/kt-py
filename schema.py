import strawberry
from typing import Optional, List

@strawberry.type
class Product:
    id: strawberry.ID
    name: str
    price: float
    description: Optional[str] = None
    
@strawberry.type
class User:
    id: strawberry.ID
    name: str
    
    @strawberry.field
    def products(self) -> List[Product]:
        return [
            Product(id=1, name="hoh", price=8324.5),
            product.get(2)
            ]
    
product = {
    1: Product(id=1, name="hoh", price=8324.5),
    2: Product(id=2, name="hoh", price=8324.5),
    3: Product(id=3, name="hoh", price=8324.5),
    4: Product(id=4, name="hoh", price=8324.5),
}

user = {
    1: User(id=1, name= "fdd"),
    2: User(id=2, name= "fdd"),
    3: User(id=3, name= "fdd")
}
    
@strawberry.type
class Query:
    @strawberry.field
    def product(self, id:int) -> Product:
        return Product(id=id, name= "krok", price=800.09)
    
    @strawberry.field
    def user(self, id:int) -> User:
        return User(id=id, name= "krok")
    
schema = strawberry.Schema(query=Query)