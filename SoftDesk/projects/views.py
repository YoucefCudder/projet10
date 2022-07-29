from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from projects.models import Project, Contributor
from projects.serializers import ProjectSerializer, ProjectDetailSerializer
from users.tests import get_current_user


class ProjectViewSet(ModelViewSet):
    serializer_class = ProjectSerializer
    detail_serializer_class = ProjectDetailSerializer
    queryset = Project.objects.all()


    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.detail_serializer_class
        return super().get_serializer_class()

    def perform_create(self, serializer):
        print(self.request.user)
        serializer.save(author_user=self.request.user)



    """def post(self, request):
        local_user = request.user
        project = Project(
            title=request.data["title"],
            description=request.data["description"],
            project_type=request.data["project_type"],
            author_user_id=local_user,
        )
        project.save()
        serialized_project = ProjectSerializer(project)
        return Response(serialized_project.data)

"""




