import requests

# URL del servidor (utiliza "localhost" o "127.0.0.1" para la dirección IP)
url = 'http://172.16.0.187:8080/'

# Realizar una solicitud GET al servidor
response = requests.get(url)

# Imprimir la respuesta del servidor
print(response.text)