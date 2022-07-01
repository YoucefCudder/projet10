from rest_framework.routers import DefaultRouter
from projects.views import ProjectViewSet
from django.urls import path, include

router = DefaultRouter()
router.register('projects', ProjectViewSet, basename='projects')


urlpatterns = [
        path('api/', include(router.urls))
]