import socket
import json
from http_parser import parse_http_request
from router import route_request 

def start_server(host='0.0.0.0', port=8080):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    try:
        server_socket.bind((host, port))
        server_socket.listen(5)
        print(f"Servidor escuchando en http://{host}:{port}")
        
        while True:
            client_socket, client_address = server_socket.accept()
            print(f"\nConexión recibida de: {client_address}")
            handle_connection(client_socket)
            
    except KeyboardInterrupt:
        print("\nApagando servidor")
    finally:
        server_socket.close()

def handle_connection(client_socket):
    try:
        request_data = client_socket.recv(1024).decode('utf-8')
        if not request_data:
            return

        # Parsear
        parsed = parse_http_request(request_data)
        
        print("Petición Recibida")
        print(json.dumps(parsed, indent=2))
        
        # El router toma una deisición 
        response = route_request(parsed)
        
        # Responder
        client_socket.send(response.encode('utf-8'))
        
    except Exception as e:
        print(f"Error en la conexión: {e}")
    finally:
        # Cerrar
        client_socket.close()

if __name__ == "__main__":
    start_server()