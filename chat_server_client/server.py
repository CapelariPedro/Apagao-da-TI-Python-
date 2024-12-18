import socket
import threading

HOST = '127.0.0.1'
PORT = 8080

clients = []

def broadcast(message, _client):
    for client in clients:
        if client != _client:
            try:
                client.send(message)
            except:
                clients.remove(client)


def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            if message:
                print(f"Mensagem recebida: {message.decode()}")
                broadcast(message, client)
        except:
            clients.remove(client)
            client.close()
            break



def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(5)
    print(f"Servidor rodando no IPv4:{HOST}, na porta: {PORT}")

    while True:
        client, addr = server.accept()
        print(f"Nova conexão: {addr}")
        clients.append(client)
        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()



if __name__ == "__main__":
    main()