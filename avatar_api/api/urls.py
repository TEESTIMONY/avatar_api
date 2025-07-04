from django.urls import path
from .views import GenerateAvatarView

urlpatterns = [
    path('generate/', GenerateAvatarView.as_view(), name='generate_avatar'),
]
