from handlers import (
    handle_welcome, 
    handle_system_time, 
    handle_auth_check, 
    handle_not_found
)

ROUTES = {
    "/welcome": handle_welcome,
    "/system/time": handle_system_time,
    "/auth/check": handle_auth_check,
}

def route_request(parsed_request):
    path = parsed_request.get("path")

    handler_function = ROUTES.get(path, handle_not_found)

    return handler_function(parsed_request)