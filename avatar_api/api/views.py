from django.shortcuts import render
import cairosvg
import base64
from io import BytesIO

# Create your views here.
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .models import Avatar
from .serializers import AvatarSerializer, UserRegistrationSerializer, UserLoginSerializer
from multiavatar.multiavatar import multiavatar
import random
from django.contrib.auth.models import User




class GenerateAvatarView(generics.CreateAPIView):
    queryset = Avatar.objects.all()
    serializer_class = AvatarSerializer

    def perform_create(self, serializer):
        seed_text = serializer.validated_data['seed_text']
        svg_data=multiavatar(seed_text,False,None)
        serializer.save(svg_data=svg_data)
        cairosvg.svg2png(bytestring=svg_data.encode('utf-8'), write_to=f"{seed_text}.png")

    def create(self,request,*args,**kwargs):
        response = super().create(request, *args,**kwargs)
        svg_data = response.data['svg_data']

        # Convert SVG to PNG
        png_buffer = BytesIO()
        cairosvg.svg2png(bytestring=svg_data.encode('utf-8'), write_to=png_buffer)
        png_base64 = base64.b64encode(png_buffer.getvalue()).decode('utf-8')
        
        # Add PNG data to response
        response.data['png_data'] = f"data:image/png;base64,{png_base64}"
        return response


class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'user_id': user.id,
            'username': user.username,
            'email': user.email,
            'token': token.key
        }, status=status.HTTP_201_CREATED)

class UserLoginView(generics.GenericAPIView):
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'user_id': user.id,
            'username': user.username,
            'email': user.email,
            'token': token.key
        }, status=status.HTTP_200_OK)

