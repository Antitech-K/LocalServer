import socket

def startServer():
    while True:
        try:
            server = socket.create_server(("127.0.0.1", 2000))
            server.listen(2)
            print ("Сервак поднялся")
            clientSocket, address = server.accept()
            data = clientSocket.recv(1024).decode("utf-8")
            content = answer(data)
            clientSocket.send(content)
            clientSocket.shutdown(socket.SHUT_WR)
            
            print(data)
        except:
            server.close()
            print("Упал сервачёк")
    

def answer(requestData):
    headers = "HTTP/1.1 200 OK\r\n content-type: text/html; charset=utf-8\r\n\r\n"
    return headers.encode("utf-8") + "All R!".encode("utf-8")

if __name__=="__main__":
    startServer()