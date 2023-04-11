from http.server import\
    BaseHTTPRequestHandler,\
    HTTPServer
import threading


class Custom_h_t_t_p_request_handler\
    (BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/hello':
            response_body = 'hello'.encode('utf-8')
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.send_header("Content-Length", str(len(response_body)))
            self.end_headers()
            self.wfile.write(response_body)
        elif self.path == '/bye':
            threading.Thread(target = h_t_t_p_server.shutdown).start()
        else:
            self.send_response(404)


h_t_t_p_server =\
    HTTPServer(
        ('localhost', 8080),
        Custom_h_t_t_p_request_handler
    )

try:
    h_t_t_p_server\
        .serve_forever()
except KeyboardInterrupt:
    pass

h_t_t_p_server\
    .server_close()