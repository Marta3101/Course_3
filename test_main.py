import requests
from requests.auth import HTTPBasicAuth



basic_auth = HTTPBasicAuth("1VQDHXQ8EF73QTHESPT7UHU9AJQPLXXL", '')


def test_check_search():
    response = requests.get("http://164.92.218.36:8080/search?controller=search&s=clothes", auth=basic_auth)
    print(response)
    assert response.text.find("clothes") >= 0

def test_check_exit():
    response = requests.get("http://164.92.218.36:8080/?mylogout=", auth=basic_auth)
    print(response)
    assert response.text.find("clothes") >= 0


def test_create_user():
    data = {
        'name': "John Doe",
        "email": "johndoe@example.com",
        "gender": "Male",
        "password": "1234567",
        "birthday": "2001 - 01 - 31"
    }
    response = requests.post("http://164.92.218.36:8080/login?create_account=1", data)
    assert response.status_code == 200

def test_check_auth():
    data = {'email': "user@gmail.com", 'password': "1234567","submitLogin": 1}
    response = requests.post("http://164.92.218.36:8080/login?back=my-account", data )
    print(response)
    assert response.status_code == 200


def test_check_communication_auth():
    data = {'from': "user@gmail.com", 'message': "help", 'fileUpload': "(binary)"}
    response = requests.post("http://164.92.218.36:8080/contact-us", data)
    print(response)
    assert response.status_code == 200

def test_check_failed_auth():
    data = {'email': "user@gmail.com", 'password': "123456","submitLogin": 1}
    response = requests.post("http://164.92.218.36:8080/login?back=my-account", data)
    print(response)
    assert response.text.find("Помилка авторизації") >= 0




