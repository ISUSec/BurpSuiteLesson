from http.server import HTTPServer, BaseHTTPRequestHandler

class Server3(BaseHTTPRequestHandler):
    def doGet(self):
        if(self.path == '/'):
            self.path = 'index.html'
        try:
            fileToOpen = open(self.path[1:]).read()
            self.send_response(200)
        except:
            fileToOpen = "file not found"
            self.send_response(200)
        self.end_headers()
        self.wfile.write(bytes(fileToOpen, 'utf-8'))

httpd = HTTPServer(('localhost', 8080), Server)
httpd.serve_forever()
