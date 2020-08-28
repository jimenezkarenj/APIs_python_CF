import requests
import json

###########################################
### 1. REALIZAR UNA PETICIÓN METODO GET ###
###########################################
"""if __name__ == '__main__':
    url = 'https://www.google.com/'
    response = requests.get(url)
    print(response)
    
    if response.status_code == 200:
        # Obtener todo el contenido que el servidor envia
        content = response.content

        file = open('google.html', 'wb')
        file.write(content)
        file.close()

        print(response.content)"""

############################################
### 2. REALIZAR UNA PETICIÓN METODO ARGS ###
############################################
"""if __name__ == '__main__':
    url = 'https://httpbin.org/get'
    # Enviar palabras de forma dinamica usando diccionarios
    args = {'nombre':'Karen', 'curso': 'python', 'nivel':'intermedio'}
    response = requests.get(url, params = args)
    print(response.url)

    if response.status_code == 200:
        content = response.content
        print(content)"""

#######################################################
### 3. OBTENER JSON QUE ENVIA EL SERVIDOR 2 FORMAS ###
#######################################################
"""if __name__ == '__main__':
    url = 'https://httpbin.org/get'
    # Enviar palabras de forma dinamica usando diccionarios
    args = {'nombre':'Karen', 'curso': 'python', 'nivel':'intermedio'}
    
    response = requests.get(url, params = args)
    print(response.url)

    if response.status_code == 200:
        
        # PRIMERA FORMA
        response_json = response.json() #Dict
        origin = response_json['origin']
        print(origin)
       
        # SEGUNDA FORMA <<USANDO LA LIBRERIA JSON>>
        response_json = json.loads(response.text)
        origin = response_json['origin']
        print(origin)"""

############################################
### 4. REALIZAR UNA PETICIÓN METODO POST ###
############################################
""""if __name__ == '__main__':
    # Crear un recurso dentro del servidor 

    url = 'https://httpbin.org/post'
    payload = {'nombre':'Karen', 'curso': 'python', 'nivel':'intermedio'}
    
    response = requests.post(url, json = payload)
    
    #json post se encarga de serializarlos
    #data entonces nosotros nos encargamos de serializarlos
    print(response.url)

    if response.status_code == 200:
        response = json.loads(response.content)
        print(json.dumps(response,indent=2, sort_keys=True))"""
        
######################
### 5. ENCABEZADOS ###
######################
"""if __name__ == '__main__':
    
    url = 'https://httpbin.org/post'
    payload = {'nombre':'Karen', 'curso': 'python', 'nivel':'intermedio'}
    headers = {'Content-Type' : 'application/json', 'access-token' : '12345'}
    
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    
    print(response.url)

    if response.status_code == 200:
        #response = json.loads(response.content)
        #print(json.dumps(response,indent=2, sort_keys=True))
        headers_response = response.headers #Dic
        server = headers_response['Server']
        print(server)"""

#####################
### 6. Metodo PUT ###
#####################
"""if __name__ == '__main__':
    
    url = 'https://httpbin.org/put'
    payload = {'nombre':'Karen', 'curso': 'python', 'nivel':'intermedio'}
    headers = {'Content-Type' : 'application/json', 'access-token' : '12345'}
    
    response = requests.put(url, data=json.dumps(payload), headers=headers)
    
    print(response.url)

    if response.status_code == 200:
        #response = json.loads(response.content)
        #print(json.dumps(response,indent=2, sort_keys=True))
        headers_response = response.headers #Dic
        server = headers_response['Server']
        print(server)"""


########################
### 7. Metodo DELETE ###
########################

if __name__ == '__main__':
    
    url = 'https://httpbin.org/delete'
    payload = {'nombre':'Karen', 'curso': 'python', 'nivel':'intermedio'}
    headers = {'Content-Type' : 'application/json', 'access-token' : '12345'}
    
    response = requests.delete(url, data=json.dumps(payload), headers=headers)
    
    print(response.url)

    if response.status_code == 200:
        headers_response = response.headers #Dic
        server = headers_response['Server']
        print(server)

## GET obtener recurso  ##
## POST crear recurso  ##
## PUT actualizar recurso  ##
## DELETE eliminar un recurso  ##
