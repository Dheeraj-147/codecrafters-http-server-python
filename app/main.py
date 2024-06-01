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
    a=req[1].split("/")
    leng=""
    if len(a)==1:
        leng=a[0]
    else:
        leng=req[1].split("echo")[1][1:]
    st="HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: "+str(len(leng))+"\r\n\r\n"+leng
    # client_socket.sendall(request)
    client_socket.sendall(bytes(st, "utf-8"))
    
if __name__ == "__main__":
    main()
