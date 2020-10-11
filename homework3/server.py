import socket, threading                                                

host = '127.0.0.1'                                                      
port = 7976                                                             

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)              
server.bind((host, port))                                               
server.listen()

clients = []
nicknames = []

def broadcast(message):                                                 #broadcast 
    for client in clients:
        client.send(message)

def handle(client):                                         
    while True:
        try:                                                            #recieve messages from client, broadcast
            message = client.recv(1024
            if message: 
                broadcast(message)
            else:
                index = clients.index(client)                           #diconnection logic
                clients.remove(client)
                client.close()
                nickname = nicknames[index]
                broadcast('{} left!'.format(nickname).encode('ascii'))
                nicknames.remove(nickname)

        except:                                                         
            
            continue

def receive():                                                          #multiple clients
    while True:
        client, address = server.accept()
        print("Connected with {}".format(str(address)))       
        client.send('NICKNAME'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)
        print("Nickname is {}".format(nickname))
        broadcast("{} joined!".format(nickname).encode('ascii'))
        client.send('Connected to server!'.encode('ascii'))
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

receive()
