from django.http import JsonResponse
from django.conf import settings
class APIKeyAuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.valid_api_key = settings.API_KEY
        self.valid_account_id = settings.ACCOUNT_ID
    def __call__(self, request):
        api_key = request.headers.get("api-key")
        account_id = request.headers.get("account-id")
        if not api_key or not account_id:
            return JsonResponse({"detail": "Missing API credentials"}, status=401)

        if api_key != self.valid_api_key or account_id != self.valid_account_id:
            return JsonResponse({"detail": "Invalid API credentials"}, status=403)

        return self.get_response(request)
