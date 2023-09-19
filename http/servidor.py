import http.server
import socketserver
import time

SERVER_IP = '172.16.0.187'
PORT = 8080

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        response_message = f'{current_time}: Grupo: Gabriel'

        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(response_message.encode('utf-8'))

with socketserver.TCPServer((SERVER_IP, PORT), MyHandler) as httpd:
    print(f"Servidor HTTP en http://{SERVER_IP}:{PORT}")
    httpd.serve_forever()