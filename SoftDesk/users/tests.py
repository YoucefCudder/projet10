import jwt
from django.contrib.auth.models import User

# Create your tests here.
from rest_framework.exceptions import AuthenticationFailed


def get_current_user(request):
    token = request.COOKIES.get("jwt")
    if not token:
        raise AuthenticationFailed("Vous n'êtes pas connecté")
    try:
        payload = jwt.decode(token, "secret", algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
        raise AuthenticationFailed("Vous avez été déconnecté")

    # Get User from PayLoad
    local_user = User.objects.filter(id=payload["id"]).first()
    return local_user
