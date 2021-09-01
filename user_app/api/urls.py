from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from user_app.views import register_view

urlpatterns = [
    path('login/', obtain_auth_token, name='login'),  # response is the token
    path('register/', register_view, name='register'),  # response is the token

]
