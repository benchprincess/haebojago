from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

urlpatterns = [
    path("", views.Users.as_view()), # api/v1/users
    path("myinfo", views.MyInfo.as_view()), # api/v1/users/myinfo

    # Authetication
    path("getToken", obtain_auth_token), # DRF token
    path("login", views.Login.as_view()), #Django Session login
    path("logout", views.Logout.as_view()), #Django Session logout
    
    # JWT Authentication
    path("login/jwt", views.JWTLogin.as_view()),
    path("login/jwt/info", views.UserDetailView.as_view()),

    # Simple JWT Authentication
    path("login/simpleJWT", TokenObtainPairView.as_view()),
    path("login/simpleJWT/refresh", TokenRefreshView.as_view()),
    path("login/simpleJWT/verify", TokenVerifyView.as_view()),
]

# {
#     "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcwOTUyMTc3NiwiaWF0IjoxNzA4MzEyMTc2LCJqdGkiOiI4MWQ0YzMxNDUxMzU0YWIzOWU3MzlkNDU5NTM3NTdiYiIsInVzZXJfaWQiOjF9.1-TyY66i9P-tz-6pprVw2PTaHbi767QojGA0oboCzZQ",
#     "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzA4MzE1Nzc2LCJpYXQiOjE3MDgzMTIxNzYsImp0aSI6IjY0ZGQzOTEzNDlkOTQ3OWY4YmU2YTEwNTI2NmI2MmRlIiwidXNlcl9pZCI6MX0.4wEreQeYYkCGq6bon_gV31xArtt54ZvKH-rCO5d8pFo"
# }