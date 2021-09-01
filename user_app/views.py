from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from user_app.api.serializers import RegistrationSerializer
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from user_app import models


@api_view(['POST'])
@permission_classes([AllowAny])  # so anyone can register
def register_view(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)

        data = {}

        if serializer.is_valid():
            account = serializer.save()

            data['response'] = "Registration successful"
            data['username'] = account.username
            token = Token.objects.get(user= account).key
            data['token'] = token

        else:
            data = serializer.errors

        return Response(data)
