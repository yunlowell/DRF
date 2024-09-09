from django.db import models

# Create your models here.

#글 작성하기
class Article(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    image = models.ImageField(upload_to='products/', null=True, blank=True) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)