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
    length=len(req)
    #req1=req[4].split("\r")[0]
    #st="HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: "+str(len(req1))+"\r\n\r\n"+req1
    # a=req[1].split("/")
    # leng=""
    # if len(a)==2 and req[1]!="/":
    #     leng=a[1]
    #     st="HTTP/1.1 404 Not Found\r\nContent-Type: text/plain\r\nContent-Length: "+str(len(leng))+"\r\n\r\n"+leng
    # elif len(a)==2 and req[1]=="/":
    #     st="HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: 0\r\n\r\n"
    # else:
    #     leng=req[1].split("echo")[1][1:]
    #     st="HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: "+str(len(leng))+"\r\n\r\n"+leng
    # client_socket.sendall(request)
    client_socket.sendall(length)
    
if __name__ == "__main__":
    main()
