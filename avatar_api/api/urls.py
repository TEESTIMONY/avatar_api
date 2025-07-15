from django.urls import path
from .views import GenerateAvatarView, UserRegistrationView, UserLoginView, CommunityAvatarShareView, CommunityAvatarListView, AvatarReactionView

urlpatterns = [
    path('generate/', GenerateAvatarView.as_view(), name='generate_avatar'),
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('community/avatars/', CommunityAvatarShareView.as_view(), name='community_avatar_share'),
    path('community/avatars/list/', CommunityAvatarListView.as_view(), name='community_avatar_list'),
    path('community/avatars/<int:avatar_id>/react/', AvatarReactionView.as_view(), name='avatar_react'),
]
