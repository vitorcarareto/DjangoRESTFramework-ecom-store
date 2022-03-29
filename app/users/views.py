from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from app.users.models import User
from app.users.serializers import UserSerializer


class ListUsers(APIView):

    def get(self, request, format=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
