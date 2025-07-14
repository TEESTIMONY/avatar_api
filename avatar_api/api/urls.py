from django.urls import path
from .views import GenerateAvatarView, UserRegistrationView, UserLoginView

urlpatterns = [
    path('generate/', GenerateAvatarView.as_view(), name='generate_avatar'),
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
]
