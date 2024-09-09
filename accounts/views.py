from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from .models import User
from .serializers import UserSerializer

# 회원가입 기능
class RegisterView(APIView):

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "회원가입이 완료되었습니다."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 프로필 조회

User = get_user_model()

class ProfileView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]  # 로그인 상태에서만 접근 가능

    def get_object(self):
        username = self.kwargs['username'] 
        user = generics.get_object_or_404(User, username=username)
        return user

    def get(self, request, *args, **kwargs):
        # 로그인한 사용자만 자신의 프로필을 조회 가능하게 할 수 있는 추가 검증
        if request.user.username != self.kwargs['username']:
            return Response({"detail": "You are not allowed to view this profile."}, status=403)
        return super().get(request, *args, **kwargs)