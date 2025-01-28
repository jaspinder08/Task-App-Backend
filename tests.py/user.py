from models.user import User 


def test_create_user():
    user = User(username ="user", email ="user@email.com" , hashed_password="password",)
    assert user.username=="user"
    assert user.emai== "user@email.com"
    assert user.hashed_password =="password"
    