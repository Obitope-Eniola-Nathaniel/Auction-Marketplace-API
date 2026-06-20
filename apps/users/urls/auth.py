from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from apps.users.views import RegisterView
from apps.users.views.register import RegisterView
from apps.users.views.logout import LogoutView


urlpatterns = [
    path( "register/", RegisterView.as_view(), name="auth-register", ),
    path("login/", TokenObtainPairView.as_view(), name="auth-login",),
    path("refresh/", TokenRefreshView.as_view(), name="auth-refresh",),
    path( "logout/", LogoutView.as_view(),name="logout",),
]
