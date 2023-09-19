import http.server
import socketserver

SERVER_IP = '172.16.0.187'
PORT = 8080

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b'Hola, como estas?')

with socketserver.TCPServer((SERVER_IP, PORT), MyHandler) as httpd:
    print(f"Servidor HTTP en http://{SERVER_IP}:{PORT}")
    httpd.serve_forever()