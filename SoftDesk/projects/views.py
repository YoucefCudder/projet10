from rest_framework.viewsets import ModelViewSet
from projects.models import Project, Contributor, Issue
from projects.serializers import ProjectSerializer, ProjectDetailSerializer, \
    IssueSerializer


class ProjectViewSet(ModelViewSet):
    serializer_class = ProjectSerializer
    detail_serializer_class = ProjectDetailSerializer

    def get_queryset(self, *args, **kwargs):
        projects_id = [contributor.project.id for contributor in
                       Contributor.objects.filter(user=self.request.user)]
        return Project.objects.filter(id__in=projects_id)

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.detail_serializer_class
        return super().get_serializer_class()

    def perform_create(self, serializer):
        project = serializer.save(author_user=self.request.user)
        Contributor(user=self.request.user, project=project,
                    role='AUTHOR').save()


class IssueViewSet(ModelViewSet):
    serializer_class = IssueSerializer

    def get_queryset(self, *args, **kwargs):
        project_id = [issue.project.id for issue in
                      Issue.objects.filter(user=self.request.user)]
        return Issue.objects.filter(id__in=project_id)

    def perform_create(self, serializer):
        serializer.save(author_user=self.request.user)
