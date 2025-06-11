import socket

PORT=14253
SERVER=socket.gethostbyname(socket.gethostname())
ADRESS= (SERVER,PORT)
FORMAT="utf-8"
BYTESIZE=1024
DISCONNECT_MESSAGE="quit"

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADRESS)

while True:
    message=client.recv(BYTESIZE).decode(FORMAT)

    if message == DISCONNECT_MESSAGE:
        client.send("Çıkış Yapıldı.".encode(FORMAT))
        break
    else:
        print(f"{message}\n")
        message=input("Mesajınız:")
        client.send(message.encode(FORMAT))

client.close()