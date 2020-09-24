from socket import *
import time

PORT = 8080
SERVER = 'localhost'
FORMAT = 'utf-8'

def createServer():
    SocKet = socket(AF_INET, SOCK_STREAM)
    try :
        SocKet.bind((SERVER, PORT))
        SocKet.listen(5)
        while(1):
            conn, address = SocKet.accept()
            print("... " + str(address))
            request = conn.recv(1024)
            if request:
                request = request.decode(FORMAT)
            else:
                print("....")
                continue 
            print(request)
            str_list = request.split(' ')
            method = str_list[0]               
            if method == "GET":
                request_file = str_list[1]
                if request_file.endswith("?v=2.2.0"):
                    request_file = request_file[request_file.index("/"): request_file.index("?")]
                request_file = request_file.lstrip('/')
               
                if (request_file == ''):
                    request_file = 'index.html'
                try:
                    file = open(request_file, 'rb')
                    response = file.read()
                    file.close()
                    header = "HTTP/1.1 200 OK\r\n"
                    if request_file.endswith(".ico"):
                        header += "Content-Type: image/ico\r\n\r\n"
                    elif request_file.endswith(".html"):
                        header += "Content-Type: text/html\r\n\r\n"
                    elif request_file.endswith(".jpg"):
                        header += "Content-Type: image/jpeg\r\n\r\n"
                    elif request_file.endswith(".js"):
                        header += "Content-Type: text/javascript\r\n\r\n" 
                    elif request_file.endswith(".css"):
                        header += "Content-Type: text/css\r\n\r\n"
                    elif request_file.endswith(".ttf"):
                        header += "Content-Type: font/ttf\r\n\r\n"   
                    elif request_file.endswith(".otf"):
                        header += "Content-Type: font/otf\r\n\r\n" 
                    elif request_file.endswith(".eot"):
                        header += "Content-Type: application/vnd.ms-fontobject\r\n\r\n" 
                    elif request_file.endswith(".svg"):
                        header += "Content-Type: image/svg+xml\r\n\r\n" 
                    elif request_file.endswith(".woff"):
                        header += "Content-Type: font/woff\r\n\r\n" 
                    elif request_file.endswith(".woff2"):
                        header += "Content-Type: font/woff2\r\n\r\n" 
                except Exception:
                    header = "HTTP/1.1 404 Not Found\r\n\r\n"
                    file = open("404.html", "rb")
                    response = file.read()
                    file.close()
            elif method == "POST":
                temp = str_list[len(str_list)-1]
                username = temp[temp.index("username") + 9: temp.index("&password")]
                password = temp[temp.index("&password") + 10: len(temp)]
                if (username == "admin" and password == "admin"):
                    header = 'HTTP/1.1 301 Moved Permanently\nLocation: info.html\n'
                else:
                    header = 'HTTP/1.1 301 Moved Permanently\nLocation: 404.html\n'
            final_res = header.encode(FORMAT)
            if (method == "GET"):
                final_res += response
            conn.send(final_res)
            conn.close()    
    except KeyboardInterrupt:
        print("\nShutting down...\n")
    
 
    print("close")
    SocKet.close()

print(SERVER)
createServer()