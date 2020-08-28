import requests

client_id = '9b40ca1180c331d607b4'
client_secret = 'ee259b7b8b0f55160ca1d8d79b5c0a6b2e55606a'

#https://github.com/login/oauth/authorize?client_id=ed28f437570e20c20410&scope=repo

#code se genera luego de ingresar a la url de arriba
code = '81c36c8d90a27f5ba051'

access_token = 'e0692e020fe29927b99920bf05efc289f92a4123' 
#access_token se genera al ejecutar el código de abajo

if __name__ == '__main__':
    url = 'https://github.com/login/oauth/access_token'
    payload = {'client_id' : client_id, 'client_secret' : client_secret, 'code' : code}
    headers = {'Accept' : 'application/json'}
    

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        response_json = response.json()

        access_token = response_json['access_token']
        print(access_token)