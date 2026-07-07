from faker import Faker

dummy = Faker()

VALID_LOGIN = {
    "title_page": "Login",
    "username": "manusiasilver",
    "password": "Test!ng123",
    "expected_result": "manusiasilver",
}

INVALID_LOGIN = {
        "title_page": "Login",
        "username": "invalid_user",
        "password": "invalid_password",
        "expected_result": "Invalid username or password!",
}

TEXTBOX_DATA = {
    "title_page": "Text Box",
    "name": dummy.name(),
    "email": dummy.email(),
    "current_address": "Jl. Seturan Raya No.10, Yogyakarta",
    "permanent_address": "Jl. Laksda Adisucipto No.123, Yogyakarta",
}

RADIO_DATA = {
    "title_page": "Radio Button",
    "expected_result_of_yes": "You have selected Yes",
    "expected_result_of_impressive": "You have selected Impressive",
}

CHECKBOX_DATA = {
    "title_page": "Check Box",
    "expected_result": [
        "home",
        "desktop",
        "documents",
        "downloads",
        "notes",
        "commands",
        "workspace",
        "office",
        "wordFile",
        "excelFile",
        "react",
        "angular",
        "veu",
        "public",
        "private",
        "classified",
        "general",
    ]
}