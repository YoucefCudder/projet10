from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from projects.models import Project
from projects.serializers import ProjectSerializer

"""test, créer  d'abord systeme utilisateurs (> JWT CHAPITRE 3 )"""


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
