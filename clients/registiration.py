import requests
from pprint import pprint

def client():
    credentials = {
        'username':'rest_deneme',
        'email':'rest_deneme@rest.com',
        'password1':'Tg123580',
        'password2':'Tg123580'
    }
    response = requests.post(url='http://127.0.0.1:8000/api/rest-auth/registiration/',
                             data=credentials,
                             )
    print('status code',response.status_code)
    response_data =response.json()
    pprint(response_data)

if __name__ == '__main__':
    client()





