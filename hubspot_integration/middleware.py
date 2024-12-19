# import logging

# logger = logging.getLogger(__name__)

# class LoggingMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response
#         logger.info("LoggingMiddleware initialized.")

#     def __call__(self, request):
#         logger.info(f"Request URL: {request.path}, Method: {request.method}")
#         response = self.get_response(request)
#         logger.info(f"Response Status Code: {response.status_code}")
#         return response