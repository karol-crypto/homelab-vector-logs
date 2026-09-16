from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class LogHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length)
        
        print(f"Log from {self.client_address[0]}:")
        try:
            json_data = json.loads(post_data.decode('utf-8'))
            print(json.dumps(json_data, indent=2))
        except json.JSONDecodeError:
            print(post_data.decode('utf-8'))
            
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"OK")

def run(server_class=HTTPServer, handler_class=LogHandler, port=8080):
    server_address = ('0.0.0.0', 8080)
    httpd = server_class(server_address, handler_class)
    print(f"Listening {port}...")
    httpd.serve_forever()

if __name__ == '__main__':
    run()


