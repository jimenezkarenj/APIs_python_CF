import requests

client_id = '9b40ca1180c331d607b4'
client_secret = 'ee259b7b8b0f55160ca1d8d79b5c0a6b2e55606a'

#https://github.com/login/oauth/authorize?client_id=ed28f437570e20c20410&scope=repo

#code se genera luego de ingresar a la url de arriba
code = '81c36c8d90a27f5ba051'
access_token = 'e0692e020fe29927b99920bf05efc289f92a4123' 

url = 'http://api.github.com/user/repos'
payload = {'name' : 'git_api_cf_comunidad'}
headers = {'Accept' : 'application/json', 'Authorization' : 'token ' + access_token}

response = requests.post(url, headers=headers, json=payload)

if response.status_code == 200:
    print(response.json())

else:
    print(response.content)