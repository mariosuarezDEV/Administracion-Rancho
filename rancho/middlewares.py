# Middleware para obtener el usuario autenticado en la petición

from django.contrib.auth.models import AnonymousUser
from django.utils.deprecation import MiddlewareMixin

class UserLoginMiddleware(MiddlewareMixin):
    def process_request(self, request):
        request.usuario_login = request.user if request.user.is_authenticated else AnonymousUser()