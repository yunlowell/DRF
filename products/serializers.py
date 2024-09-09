from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"

    def validate(self, data):
        if not data.get('title') or not data.get('content'):
            raise serializers.ValidationError("제목과 내용을 입력하세요.")
        if not data.get('image'):
            raise serializers.ValidationError("상품 이미지를 첨부하세요.")
        return data