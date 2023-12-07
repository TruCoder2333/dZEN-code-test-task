from .models import Comment
from .serializers import CommentSerializer
from captcha.models import CaptchaStore
from captcha.helpers import get_safe_now
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status



class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        captcha_key = serializer.validated_data.get('captcha_key')
        captcha_response = serializer.validated_data.get('captcha_response')

        if not self.validate_captcha(captcha_key, captcha_response):
            return Response({"captcha": ["Invalid CAPTCHA."]}, status=status.HTTP_400_BAD_REQUEST)

        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


    def validate_captcha(self, captcha_key, captcha_response):
        try:
            captcha = CaptchaStore.objects.get(hashkey=captcha_key, expiration__gt=get_safe_now())
        except CaptchaStore.DoesNotExist:
            return False

        if captcha.response == captcha_response.lower():
            captcha.delete()
            return True
        else:
            return False
