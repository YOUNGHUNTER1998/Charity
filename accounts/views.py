from rest_framework import generics
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import UserSerializer


class LogoutAPIView(APIView):
    pass


class UserRegistration(APIView):
    def post(self, request):
        user_serializer = UserSerializer(data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response({'message': 'user added successfully'}, status=status.HTTP_200_OK)
        return Response({'message': user_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


