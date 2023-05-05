import usocket as socket

HOST = ''
PORT = 8888

def handle_client(client):
    while True:
        try:
            data = client.recv(1024)
            if not data:
                break
            client.sendall(data)
        except Exception as e:
            print("Error: ", e)
            break
    client.close()

if __name__ == '__main__':
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(5)

    print('Server started at', server.getsockname())

    while True:
        client, address = server.accept()
        print("Accepted connection from", address)
        handle_client(client)
