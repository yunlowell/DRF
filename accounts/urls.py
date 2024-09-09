from rest_framework_simplejwt.views import(
    TokenObtainPairView,
    TokenRefreshView,
)
from django.urls import path
from .views import RegisterView, ProfileView



app_name = "accounts"
urlpatterns = [
    path("", RegisterView.as_view(), name='register'),
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name='token_refresh'),
    path("<str:username>/", ProfileView.as_view(), name='profile'),
]