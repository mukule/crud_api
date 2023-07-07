from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth import get_user_model

User = get_user_model()

class BasicAuthenticationWithEmail(BaseAuthentication):
    def authenticate(self, request):
        email = request.META.get('HTTP_AUTHORIZATION_EMAIL')
        password = request.META.get('HTTP_AUTHORIZATION_PASSWORD')

        if not email or not password:
            raise AuthenticationFailed('Invalid credentials')

        try:
            user = User.objects.get(email=email)
            if user.check_password(password):
                return (user, None)
            else:
                raise AuthenticationFailed('Invalid credentials')
        except User.DoesNotExist:
            raise AuthenticationFailed('Invalid credentials')
