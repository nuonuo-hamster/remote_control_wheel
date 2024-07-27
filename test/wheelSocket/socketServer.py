import socket

def serverOpen():

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 8889))
    server_socket.listen(5)
    return server_socket

def dataTransport(server_socket):
    client_socket, addr = server_socket.accept()
    try:
        while True:
            data = client_socket.recv(1024).decode()
            if not data:
                break
            print(f"Received data: {data}")
    finally:
        client_socket.close()

def main():

    print("open server")
    server_socket = serverOpen()

    while(True):
        try:
            print("Wait for client...")
            dataTransport(server_socket)
            print("client offline")
        except:
            pass

if __name__ == '__main__':

    main()