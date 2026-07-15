import pytest
from models.user import User

def test_user_creation():
    user = User("Bob", "bob@gmail.com")
    assert user.name == "Bob"
    assert user.email == "bob@gmail.com"

def test_email_validation():
    with pytest.raises(ValueError):
        User("Bob", "bademail")
    
    