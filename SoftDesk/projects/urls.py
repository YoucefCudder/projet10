from rest_framework.routers import DefaultRouter
from projects.views import ProjectViewSet
from django.urls import path


urlpatterns = [
        path('', ProjectViewSet.as_view(),  name='projects' )
]