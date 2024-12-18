import socket

def start_peer1():
    #Configura as conexões 
    peer1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    peer1.bind(('localhost', 8081))
    peer1.listen()

    #Aguardando conexões
    print('Peer1 Aguardando conexões...')
    conn, addr = peer1.accept()
    #Conexão efetuada
    print(f'Conectado a {addr}')

    while True:
        #Envia dados
        message = input("Você: ")
        conn.send(message.encode('utf-8'))
        #Recebe dados
        response = conn.recv(1024).decode('utf-8')
        print(f'Outro: {response}')

start_peer1()
