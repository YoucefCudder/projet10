from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from projects.models import Project, Contributor, Issue, Comment
from projects.serializers import (
    ProjectSerializer,
    ProjectDetailSerializer,
    IssueSerializer,
    CommentsSerializer,
    ContributorsSerializer,
)


class ProjectViewSet(ModelViewSet):
    serializer_class = ProjectSerializer
    detail_serializer_class = ProjectDetailSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self, *args, **kwargs):
        projects_id = [
            contributor.project.id
            for contributor in Contributor.objects.filter(user=self.request.user)
        ]
        return Project.objects.filter(id__in=projects_id)

    def get_serializer_class(self):
        if self.action == "retrieve":
            return self.detail_serializer_class
        return super().get_serializer_class()

    def perform_create(self, serializer):
        project = serializer.save(author_user=self.request.user)
        Contributor(user=self.request.user, project=project, role="AUTHOR").save()


class IssueViewSet(ModelViewSet):
    serializer_class = IssueSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self, *args, **kwargs):
        return Issue.objects.filter(project=int(self.kwargs["nested_1_pk"]))

    def perform_create(self, serializer):
        project = Project.objects.get(id=int(self.kwargs["nested_1_pk"]))
        serializer.save(project=project, author_user=self.request.user)


class CommentViewSet(ModelViewSet):
    serializer_class = CommentsSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self, *args, **kwargs):
        return Comment.objects.filter(issue=int(self.kwargs["nested_2_pk"]))

    def perform_create(self, serializer):
        issue = Issue.objects.get(id=int(self.kwargs["nested_2_pk"]))

        serializer.save(author_user=self.request.user, issue=issue)


class ContributorViewSet(ModelViewSet):
    serializer_class = ContributorsSerializer

    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Contributor.objects.filter(project=int(self.kwargs["nested_1_pk"]))
