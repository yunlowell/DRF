from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Article
from .serializers import ArticleSerializer

# Create your views here.
# 글 목록 조회
@api_view(["GET"])
def article_list(request):
    articles = Article.objects.all()
    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data)

# 글 상세 조회
@api_view(["GET"])
def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    serializer = ArticleSerializer(article)
    return Response(serializer.data)