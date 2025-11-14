import json
from datetime import datetime
from http_parser import send_http_response

# Token
SECRET_TOKEN = "tilin007"

def handle_welcome(request):
    return send_http_response(200, "SV modular")

def handle_system_time(request):
    now = datetime.now()
    # ISO 8601 formato estándar para APIs
    data = {
        "timestamp": now.isoformat(),
        "timezone": now.astimezone().tzname()
    }
    json_content = json.dumps(data, indent=2)
    return send_http_response(200, json_content, content_type='application/json')

def handle_auth_check(request):
    headers = request.get("headers", {})
    
    token = headers.get("TokenPass") 
    
    if not token:
        return send_http_response(401, "Header 'TokenPass' no encontrado.")
    
    if token == SECRET_TOKEN:
        return send_http_response(200, "Autenticacion exitosa")
    else:
        return send_http_response(401, "Token invalido o incorrecto")

def handle_not_found(request):
    path = request.get("path")
    return send_http_response(404, f"Recurso en '{path}' no fue encontrado.")