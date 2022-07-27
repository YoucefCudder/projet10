from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from projects.models import Project
from projects.serializers import ProjectSerializer
from users.serializers import MyTokenObtainPairSerializer
from users.tests import get_current_user


class ProjectViewSet(ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()

    def get_queryset(self, *args, **kwargs):
        return Project.objects.filter(author_user_id=self.request.user)

    """def post(self, request):
        user = User(request)
        # Create project from Post data
        project = Project(
            title=request.data["title"],
            description=request.data["description"],
            project_type=request.data["project_type"],
            author_user_id=request.user,
        )
        project.save(False)
        print(project)
        serialized_project = ProjectSerializer(project)
        return Response(serialized_project.data)"""

    def perform_create(self, serializer):
        return serializer.save(author_user_id=self.request.user)