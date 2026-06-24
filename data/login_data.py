VALID_LOGIN = {
    "username": "tomsmith",
    "password": "SuperSecretPassword!",
    "expected": "You logged into a secure area!"
}

INVALID_LOGIN = [
    {
        "username": "invalid_user",
        "password": "invalid_password",
        "expected": "Your username is invalid!"
    },
    {
        "username": "tomsmith",
        "password": "wrong_password",
        "expected": "Your password is invalid!"
    }
]