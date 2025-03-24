import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect(("www.example.com", 80))
    # Thêm header "Host"
    request = b"GET / HTTP/1.1\r\nHost: www.example.com\r\n\r\n"
    sock.sendall(request)
    response = sock.recv(4096)
    print(response.decode())
