# serializers.py
from rest_framework import serializers
from .models import User


# 회원가입
#  username, 비밀번호, 이메일, 이름, 닉네임, 생일 필수 입력 / 성별, 자기소개 생략 가능

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['아이디', '비밀번호', '이메일', '이름', '닉네임', '생일', '성별', '자기소개']
        extra_kwargs = {
            '비밀번호': {'write_only': True}, # 비밀번호는 응답에 표시되지 않도록 설정
        }
    # 이메일 유효성 검사
    def validate_이메일(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("이 이메일은 이미 사용 중입니다.")
        return value

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['아이디'],
            password=validated_data['비밀번호'],
            email=validated_data['이메일'],
            name=validated_data['이름'],
            nickname=validated_data['닉네임'],
            birthday=validated_data['생일'],
            gender=validated_data.get('성별', ''),
            bio=validated_data.get('자기소개', '')
        )
        return user

