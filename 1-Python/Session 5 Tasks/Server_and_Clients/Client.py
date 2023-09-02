import socket

def send_message():
    host = '127.0.0.1'  # Server IP address
    port = 12345        # Server port number

    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    client_socket.connect((host, port))

    while True:
        # Send data to the server
        message = input("Enter a message: ")
        client_socket.send(message.encode('utf-8'))

        # Receive the response from the server
        response = client_socket.recv(1024).decode('utf-8')
        print("Server response: {}".format(response))

    # Close the socket
    client_socket.close()

send_message()
