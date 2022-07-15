from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from projects.models import Project
from projects.serializers import ProjectSerializer

"""test, créer  d'abord systeme utilisateurs (> JWT CHAPITRE 3 )"""


class ProjectViewSet(APIView):
    serializer_class = ProjectSerializer

    def get(self, *args, **kwargs):
        queryset = Project.objects.all()
        serializer = ProjectSerializer(queryset)
        return Response(serializer.data)