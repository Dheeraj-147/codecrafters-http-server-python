#Uncomment this to pass the first stage
import socket
import threading
import os
import argparse

def reply(req, code, body="", headers={},content_type="text/plain"):
    b_reply = b""
    if code == 200:
        b_reply += b"HTTP/1.1 200 OK\r\n"
    elif code == 201:
        b_reply += b"HTTP/1.1 201 Created\r\n"
    elif code == 404:
        b_reply += b"HTTP/1.1 404 Not Found\r\n"
    elif code == 500:
        b_reply += b"HTTP/1.1 500 Internal Server Error\r\n"

    if "Content-Type" not in headers:
        headers["Content-Type"] = content_type
    if body != b"":
        headers["Content-Length"] = str(len(body))
    for key, val in headers.items():
        b_reply += bytes(key, "utf-8") + b": " + bytes(val, "utf-8") + b"\r\n"
    b_reply += b"\r\n" + bytes(body, "utf-8")
    return b_reply

def handle_request(conn, req,directory):
    if req["path"] == "/":
        return reply(req, 200)
    elif req["path"].startswith("/files/") and req["method"] == "POST":
        filename=req["path"][7:]
        filepath=os.path.join(directory,filename)
        with open(filepath,"wb") as f:
            body=f.write(req["body"])
        return reply(req,201,"",content_type="application/octet-stream")
    elif req["path"].startswith("/files/") and req["method"] == "POST":
        filename=req["path"][7:]
        filepath=os.path.join(directory,filename)
        if os.path.isfile(filepath):
            with open(filepath,"r") as f:
                body=f.read()
            return reply(req,200,body,content_type="application/octet-stream")
        else:
            return reply(req,404,content_type="application/octet-stream")
    elif req["path"].startswith("/echo/"):
        return reply(req, 200, req["path"][6:])
    elif req["path"] == "/user-agent":
        ua = req["headers"]["User-Agent"]
        return reply(req, 200, ua)
    else:
        return reply(req, 404)

def handle_client(client_socket,directory):
    request = client_socket.recv(1024).decode("utf-8")
    headers ,body = request.split("\r\n\r\n", 1)
    request_line,*header_lines= headers.split("\r\n")
    method, path, _ = request_line.split(" ")
    headers_dict = dict(h.split(": ", 1) for h in header_lines if h)

    req = {
        "method": method,
        "path": path,
        "headers": headers_dict,
        "body": body.encode("utf-8")
    }

    response = handle_request(client_socket, req,directory)
    client_socket.sendall(response)
    client_socket.close()

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--directory",default=".")
    args=parser.parse_args()

    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)
    
    while True:
        client_socket,address=server_socket.accept() # wait for client
        client_thread=threading.Thread(target=handle_client,args=(client_socket,args.directory))
        client_thread.start()
    
if __name__ == "__main__":
    main()
