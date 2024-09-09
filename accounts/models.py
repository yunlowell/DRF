from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

# 회원가입
class User(AbstractUser):
    name = models.CharField(max_length=10, default='익명')
    nickname = models.CharField(max_length=10, unique=True, default='닉네임을 설정해주세요')
    birthday = models.DateField(default='1990-01-01')
    gender = models.CharField(max_length=10, blank=True, null=True)
    bio = models.TextField(max_length=200, blank=True, null=True)