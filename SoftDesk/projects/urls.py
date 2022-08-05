from rest_framework.routers import DefaultRouter

from projects import views
from django.urls import path, include
from rest_framework import routers

from projects.views import ProjectViewSet

router = routers.SimpleRouter()
# Puis lui déclarons une url basée sur le mot clé ‘category’ et notre view
# afin que l’url générée soit celle que nous souhaitons ‘/api/category/’
router.register('projects', ProjectViewSet, basename='projects')
router.register('projects/<int:pk>', ProjectViewSet, basename='detail')



urlpatterns = [
        #path('', ProjectViewSet.as_view(),  name='projects' ),
        path('', include(router.urls)),

        ]