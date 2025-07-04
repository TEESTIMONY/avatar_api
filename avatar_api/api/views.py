from django.shortcuts import render
import cairosvg
import base64
from io import BytesIO

# Create your views here.
from rest_framework import generics
from .models import Avatar
from .serializers import AvatarSerializer
from multiavatar.multiavatar import multiavatar
import random




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

