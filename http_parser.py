def parse_http_request(request):
    
    lines = request.split('\r\n')
    
    request_line = lines[0]
    method, path, version = request_line.split(' ')
    
    headers = {}
    body_start_index = 1
    for i, line in enumerate(lines[1:], start=1):
        if line == "": # fin de las cabeceras
            body_start_index = i + 1
            break
        if ":" in line:
            key, value = line.split(':', 1)
            headers[key.strip()] = value.strip()
    
    return {
        'method': method,
        'path': path,
        'version': version,
        'headers': headers, # cabeceras ya parceadas
    }

def send_http_response(status_code, content, content_type='text/plain'):
    status_messages = {
        200: 'OK',
        401: 'Unauthorized', 
        404: 'Not Found',
        500: 'Internal Server Error'
    }
    
    response = f"HTTP/1.1 {status_code} {status_messages.get(status_code, 'Unknown Status')}\r\n"
    response += f"Content-Type: {content_type}\r\n"
    response += f"Content-Length: {len(content)}\r\n"
    response += "Connection: close\r\n" 
    response += f"\r\n"
    response += content
    
    return response