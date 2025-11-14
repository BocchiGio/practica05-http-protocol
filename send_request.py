import socket

def send_test_request(request_str):
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(('localhost', 8080))
        
        print(f"Enviando..\n{request_str.strip()}")
        client_socket.send(request_str.encode())
        
        response = client_socket.recv(4096).decode()
        print(f"Recibido\n{response}\n")
        
    except ConnectionRefusedError:
        print("Error: No se pudo conectar.\n")
    finally:
        client_socket.close()

# ruta de bienvenida
request_welcome = (
    "GET /welcome HTTP/1.1\r\n"
    "Host: localhost\r\n"
    "\r\n"
)
send_test_request(request_welcome)

# ruta de API
request_api = (
    "GET /system/time HTTP/1.1\r\n"
    "Host: localhost\r\n"
    "\r\n"
)

send_test_request(request_api)

# Ruta auth sin token
request_auth_fail = (
    "GET /auth/check HTTP/1.1\r\n"
    "Host: localhost\r\n"
    "\r\n"
)

send_test_request(request_auth_fail)

# Auth con token correcto
request_auth_success = (
    "GET /auth/check HTTP/1.1\r\n"
    "Host: localhost\r\n"
    "TokenPass: tilin2007\r\n"
    "\r\n"
)

send_test_request(request_auth_success)