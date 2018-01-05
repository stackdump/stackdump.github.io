"""
quick and dirty webserver for development
"""
import SimpleHTTPServer
import SocketServer

PORT = 8800

if __name__ == '__main__':
    Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
    httpd = SocketServer.TCPServer(("", PORT), Handler)
    print 'running dev server: http://127.0.0.1:%s/' % PORT
    httpd.serve_forever()
