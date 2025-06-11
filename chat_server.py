import socket

PORT=14253
SERVER=socket.gethostbyname(socket.gethostname())
ADRESS= (SERVER,PORT)
FORMAT="utf-8"
BYTESIZE=1024
DISCONNECT_MESSAGE="Quit."

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(ADRESS)

server.listen()
print("Server Çalışıyor..\n")


client_socket, client_adress = server.accept()
client_socket.send("Server Bağlantınız Yapıldı.\n".encode(FORMAT))

while True:
    message=client_socket.recv(BYTESIZE).decode(FORMAT)

    if message == DISCONNECT_MESSAGE:
        client_socket.send("Çıkış Yapıldı.".encode(FORMAT))
        break

    else:
        print(f"{message}\n")
        message=input("Mesajınız:")
        client_socket.send(message.endcode(FORMAT))

client_socket.close()