from fastapi import Body, FastAPI
from typing import Union, Any
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None


class User(BaseModel):
    user_id: int
    name: str
    surname: str
    email: str
    age: int


app = FastAPI()

user_list = [
    User(user_id=1, name="John", surname="Doe", email="johnadas@mail.com", age=30),
    User(user_id=2, name="Jane", surname="Doe", email="jane@email.com", age=25),
    User(user_id=3, name="Alice", surname="Smith", email="sdasd@email.com", age=28),
]


@app.get("/users/{user_id}/item/{item_id}")
async def root(
    user_id: int,
    item_id: int,
    needy: str,
    q: Union[str, None] = None,
    short: bool = False,
) -> dict[str, int | str | bool]:
    if q:
        return {
            "user_id": user_id,
            "item_id": item_id,
            "query": q,
            "short": short,
            "needy": needy,
        }
    if not short:
        return {
            "user_id": user_id,
            "item_id": item_id,
            "story": "This is a long story about the user and item. they are very important.  because they are the user and item.",
        }
    return {
        "user_id": user_id,
        "item_id": item_id,
        "story_highlight": "This is a short story about the user and item.",
    }


@app.put("/items/{items_id}")
async def create_item(
    item: Item, items_id: int
) -> dict[Union[str, dict[str, Any]], int]:
    return {"items id": items_id, **item.model_dump()}


@app.get("/users/{users_id}")
async def show_users(users_id: int) -> list[User]:
    return [user for user in user_list if users_id == user.user_id]


class CombinedResponse(BaseModel):
    category: str
    item: Item
    user: User


@app.put("/category/{category_id}")
async def update_item(
    category_id: int, item: Item, user: User
) -> dict[str, Union[int, Item, User]]:
    results: dict[str, Union[int, Item, User]] = {
        "item_id": category_id,
        "item": item,
        "user": user,
    }
    return results
