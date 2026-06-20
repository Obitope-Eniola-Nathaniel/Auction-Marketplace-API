from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is None:
        return None

    detail = response.data.get("detail", response.data) if isinstance(response.data, dict) else response.data

    response.data = {
        "success": False,
        "error": {
            "code": getattr(exc, "default_code", "error"),
            "message": detail,
        },
    }
    return response
