import requests

if __name__ == "__main__":
    url = 'https://api.github.com/user'

    session = requests.session()
    session.auth = ('jimenezkarenj@gmail.com', '*********')

    response = session.get(url)
    
    if response.ok:
        response = session.get('https://github.com/jimenezkarenj/APIs_python_CF')
        
        if response.ok:
            print(response.content)
            print(response.cookies)
"""
    if response.ok:
        #ver el contenido de la cuenta
        print(response.content)
    else:
        #si esta mal las credenciales genera el siguiente error
        print(response.content)"""
    
         