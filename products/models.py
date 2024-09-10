from django.db import models
from django.conf import settings 
# Create your models here.

#글 작성하기
class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # 작성자 필드
    title = models.CharField(max_length=50)
    content = models.TextField()
    image = models.ImageField(upload_to='products/', null=True, blank=True) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)