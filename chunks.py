import requests
import json

if __name__ == '__main__':
    url = 'https://thehappypuppysite.com/wp-content/uploads/2018/02/lemon-beagle.jpg'

    response = requests.get(url, stream = True) #Realiza la petición sin descargar el contenido
    with open('imagen.jpg', 'wb') as file:
        for chunk in response.iter_content(): #Descarga el contenido poco a poco
            file.write(chunk)
   
    response.close()