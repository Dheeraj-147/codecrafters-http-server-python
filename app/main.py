#Uncomment this to pass the first stage
import socket


def main():
    #You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    #Uncomment this to pass the first stage
    
    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)
    client_socket,address=server_socket.accept() # wait for client
    request = client_socket.recv(1024).decode("utf-8")
    request_line=request.split("\n")[0]
    req=request_line.split(" ")
    leng=req[1].split("echo")[1][1:]
    str="HTTP/1.1 200 OK\r\n\r\nContent-Type: text/plain\r\nContent-Length: "+str(len(leng))+"\r\n\r\n"+leng
    # client_socket.sendall(request)
    client_socket.sendall(bytes(str, "utf-8"))
    
if __name__ == "__main__":
    main()
