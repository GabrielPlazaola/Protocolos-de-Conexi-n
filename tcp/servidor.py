# Servidor
import socket
import time

# Configurar el servidor
server_ip = '127.16.0.187'
server_port = 8080

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind((server_ip, server_port))

# Escuchar conexiones entrantes
server_socket.listen(1)

print(f"Esperando conexiones en {server_ip}:{server_port}...")

# Aceptar la conexión entrante
client_socket, client_address = server_socket.accept()
print(f"Conexión establecida con {client_address}")

current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
response = f"{current_time}: Grupo: Gabriel"
client_socket.send(response.encode())

# Cerrar la conexión
client_socket.close()