#!/usr/bin/env python
# Reflects the requests from HTTP methods GET, POST, PUT, and DELETE
# Written by Nathan Hamiel (2010, https://gist.github.com/huyng/814831)
# Modified by jimni

from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler

class RequestHandler(BaseHTTPRequestHandler):
        
    def do_POST(self):

        print(self.log_date_time_string() + ' from '
              + str(self.client_address[0]) + ':'
              + str(self.client_address[1]))
        print("----- Request Start ----->\n")
        print(self.command + ' ' + self.path + ' ' + self.request_version)

        content_length = self.headers.getheaders('content-length')
        length = int(content_length[0]) if content_length else 0
        
        print(self.headers)
        if length > 0: print(self.rfile.read(length))
        print("<----- Request End -----\n")
        
        self.send_response(200)
        self.end_headers()
        self.wfile.write("OK")

    do_GET = do_POST
    do_PUT = do_POST
    do_DELETE = do_GET
        
def main():
    port = 8080
    print('Listening all interfaces on port %s\n' % port)
    server = HTTPServer(('', port), RequestHandler)
    server.serve_forever()

        
if __name__ == "__main__":
    main()
