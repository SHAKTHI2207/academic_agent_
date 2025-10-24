# api/middleware/logging.py
from starlette.middleware.base import BaseHTTPMiddleware
import time

class RequestLogger(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        start_time = time.time()
        response = await call_next(request)
        duration = round(time.time() - start_time, 2)
        print(f"[LOG] {request.method} {request.url.path} → {response.status_code} in {duration}s")
        return response
