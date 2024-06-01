#Uncomment this to pass the first stage
import socket


def main():
    #You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    #Uncomment this to pass the first stage
    
    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)
    client_socket,address=server_socket.accept() # wait for client
    request = client_socket.recv(1024).decode("utf-8")
    request=request.split(" ")[0]
    # client_socket.sendall(request)
    if request[1] == "/":
        client_socket.sendall(b"HTTP/1.1 200 OK\r\n\r\n")
    else:
        client_socket.sendall(b"HTTP/1.1 404 Not Found\r\n\r\n")
if __name__ == "__main__":
    main()
