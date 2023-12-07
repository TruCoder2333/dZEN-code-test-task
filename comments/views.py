from .models import Comment
from .serializers import CommentSerializer
from captcha.models import CaptchaStore
from django.utils import timezone
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status



class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

