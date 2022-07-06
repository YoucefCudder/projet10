from django.template.defaulttags import url
from django.urls import path
from .views import CreateUserAPIView


urlpatterns = [
    path('signup/', CreateUserAPIView.as_view()),
]