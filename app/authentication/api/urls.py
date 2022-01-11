from django.urls.conf import path
from authentication.api import views


urlpatterns = [
    path('register', views.Register.as_view()),
    path('login', views.Login.as_view())
]
