from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from .models import Article
from .serializers import ArticleSerializer
# Create your views here.
# 글 목록 조회, 글 생성
class ArticleListAPIView(APIView):


    def get(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)
    
    # user가 아니면 기능 접근 제한

    def post(self, request):
        self.permission_classes = [IsAuthenticated]
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 글 상세 조회, 수정, 삭제
class ArticleDetailAPIView(APIView):

    permission_classes = [IsAuthenticated]


    def get_object(self, pk):
        return get_object_or_404(Article, pk=pk)
    
    def get(self, request, pk):
        article = self.get_object(pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    
    def put(self, request, pk):
        article = self.get_object(pk)
        if article.user != request.user:  # 게시글 작성자 확인
            return Response({"detail": "수정 권한이 없습니다."}, status=status.HTTP_403_FORBIDDEN)
        
        serializer = ArticleSerializer(article, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        
    def delete(self, request, pk):
        article = self.get_object(pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)