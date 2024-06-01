#Uncomment this to pass the first stage
import socket
def reply(req, code, body="", headers={}):
    b_reply = b""
    if code == 200:
        b_reply += b"HTTP/1.1 200 OK\r\n"
    elif code == 404:
        b_reply += b"HTTP/1.1 404 Not Found\r\n"
    elif code == 500:
        b_reply += b"HTTP/1.1 500 Internal Server Error\r\n"

    if "Content-Type" not in headers:
        headers["Content-Type"] = "text/plain"
    if body != "":
        headers["Content-Length"] = str(len(body))
    for key, val in headers.items():
        b_reply += bytes(key, "utf-8") + b": " + bytes(val, "utf-8") + b"\r\n"
    b_reply += b"\r\n" + bytes(body, "utf-8")
    return b_reply

def handle_request(conn, req):
    if req["path"] == "/":
        return reply(req, 200)
    elif req["path"].startswith("/echo/"):
        return reply(req, 200, req["path"][6:])
    elif req["path"] == "/user-agent":
        ua = req["headers"]["User-Agent"]
        return reply(req, 200, ua)
    else:
        return reply(req, 404)

def main():
    #You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    #Uncomment this to pass the first stage
    
    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)
    client_socket,address=server_socket.accept() # wait for client
    request = client_socket.recv(1024).decode("utf-8")
    request_line, headers = request.split("\r\n", 1)
    method, path, _ = request_line.split(" ")
    headers_dict = dict(h.split(": ", 1) for h in headers.split("\r\n") if h)

    req = {
        "path": path,
        "headers": headers_dict
    }

    response = handle_request(client_socket, req)
    client_socket.sendall(response)
    
if __name__ == "__main__":
    main()
