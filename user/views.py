from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from django.contrib.auth import login, logout, authenticate

from user.models import User as UserModel

# Create your views here.
class UserView(APIView):

    permission_classes = [permissions.AllowAny]

    # 사용자 정보 조회
    def get(self, request):

        return Response({"message": "get method!"})

    # 회원가입
    def post(self, request):
        username = request.data.get('username', '')
        password = request.data.get('password', '')
        print(username,password)
        UserModel.objects.create_user(request, username=username, password=password)
        return Response({"message": "post method!"})

    # 회원 정보 수정
    def put(self, request):
        
        return Response({"message": "put method!"})

    # 회원 탈퇴
    def delete(self, request):

        return Response({"message": "delete method!"})