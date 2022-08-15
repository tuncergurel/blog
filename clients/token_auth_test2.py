import requests
from pprint import pprint

def client():
    # credentials = {
    #     'username':'yedek',
    #     'password':'Tg123580'
    # }

    token = 'Token b72b35b64de93b69c3f6198b7d736fed3fa59aa1'
    headers = {'Authorization':token,}

    response = requests.get(url='http://127.0.0.1:8000/api/kullanici/',
                             headers=headers,
                             # data=credentials,
                             )
    print('status code',response.status_code)
    response_data =response.json()
    pprint(response_data)

if __name__ == '__main__':
    client()

