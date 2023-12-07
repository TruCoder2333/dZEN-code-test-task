from rest_framework import serializers
from .models import Comment

class CommentSerializer(serializers.ModelSerializer):
    replies = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    #captcha_key = serializers.CharField(write_only=True, required=False)
    #captcha_response = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = Comment
        fields = ['id', 'author', 'email', 'text', 'created_at', 'parent', 'replies']