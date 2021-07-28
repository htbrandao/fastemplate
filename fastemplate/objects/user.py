from pydantic import BaseModel


class User(BaseModel):
    """
    Schema to represent a user when dealing with authentication.
    """
    username: str
    full_name: str
    owner: bool
