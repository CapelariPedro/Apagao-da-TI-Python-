import socket

def start_peer2():
    #Configura as conexões 
    peer2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    peer2.connect(('localhost', 8081))

    while True:
        response = peer2.recv(1024).decode('utf-8')
        print(f'Outro: {response}')
        message = input('Você: ')
        peer2.send(message.encode('utf-8'))

start_peer2()
