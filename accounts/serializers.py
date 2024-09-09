# serializers.py
from rest_framework import serializers
from .models import User


# 회원가입
#  username, 비밀번호, 이메일, 이름, 닉네임, 생일 필수 입력 / 성별, 자기소개 생략 가능

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'name', 'nickname', 'birthday', 'gender', 'bio']
        extra_kwargs = {
            'password': {'write_only': True},
        }
    # 이메일 유효성 검사
    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("이 이메일은 이미 사용 중입니다.")
        return value

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email'],
            name=validated_data['name'], 
            nickname=validated_data['nickname'],
            birthday=validated_data['birthday'],
            gender=validated_data.get('gender', ''),
            bio=validated_data.get('bio', '')
        )
        return user