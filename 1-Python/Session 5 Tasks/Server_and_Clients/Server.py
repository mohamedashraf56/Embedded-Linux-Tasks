import socket
import threading

def handle_client(client_socket):
    # This function handles communication with a single client
    while True:
        # Receive data from the client
        data = client_socket.recv(1024).decode('utf-8')
        if not data:
            break
        print(f"Received from client: {data}")

        # Send a response back to the client
        response = f"Server received: {data}"
        client_socket.send(response.encode('utf-8'))

    # Close the client socket
    client_socket.close()

def start_server():
    host = '127.0.0.1'  # Server IP address
    port = 12345  # Server port number

    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to a specific address and port
    server_socket.bind((host, port))

    # Listen for incoming connections
    server_socket.listen(5)
    print("Server listening on {}:{}".format(host, port))

    while True:
        # Accept a client connection
        client_socket, addr = server_socket.accept()
        print("Connected to client: {}".format(addr))

        # Create a new thread for each client
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()

start_server()
