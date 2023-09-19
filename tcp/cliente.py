import socket

# Configurar el cliente
server_ip = '127.16.0.187'
server_port = 8080

# Crear un socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conectar al servidor
client_socket.connect((server_ip, server_port))
print(f"Conectado al servidor en {server_ip}:{server_port}")

while True:
    message = input("Escribe tu mensaje: ")
    client_socket.send(message.encode())

    data = client_socket.recv(1024)
    print(f"Respuesta del servidor: {data.decode()}")

# Cerrar la conexión
client_socket.close()