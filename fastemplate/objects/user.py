from dataclasses import dataclass

@dataclass
class User:
    """
    Schema to represent a user when dealing with authentication.
    """
    username: str
    full_name: str
    owner: bool
