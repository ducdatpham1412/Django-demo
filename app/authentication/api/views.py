from rest_framework_simplejwt.exceptions import TokenError
from authentication import models
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from authentication.api import serializers
from django.contrib.auth.hashers import make_password, check_password


class Register(GenericAPIView):
    def post(self, request):
        username = request.data['username']
        password = request.data['password']

        encrypt_password = make_password(password)

        # save user to database
        user = models.User(username=username, password=encrypt_password)
        user.save()

        return Response(None, status=status.HTTP_200_OK)


class Login(GenericAPIView):
    def post(self, request):
        username = request.data['username']
        password = request.data['password']

        user = models.User.objects.get(username=username)
        check = check_password(password, user.password)

        return Response(check, status=status.HTTP_200_OK)
