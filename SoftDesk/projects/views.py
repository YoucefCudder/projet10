from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from projects.models import Project, Contributor, Issue, Comment
from projects.serializers import ProjectSerializer, ProjectDetailSerializer, \
    IssueSerializer, CommentsSerializer, ContributorsSerializer


class ProjectViewSet(ModelViewSet):
    serializer_class = ProjectSerializer
    detail_serializer_class = ProjectDetailSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self, *args, **kwargs):
        print(self.request.user.id, "§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§")
        projects_id = [contributor.project.id for contributor in
                       Contributor.objects.filter(user=self.request.user)]
        return Project.objects.filter(id__in=projects_id)

    def get_serializer_class(self):
        print(self.request.user, "§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§")

        if self.action == 'retrieve':
            return self.detail_serializer_class
        return super().get_serializer_class()

    def perform_create(self, serializer):
        print(self.request, "§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§")

        project = serializer.save(author_user=self.request.user)
        Contributor(user=self.request.user, project=project,
                    role='AUTHOR').save()


class IssueViewSet(ModelViewSet):
    serializer_class = IssueSerializer
    permission_classes = [IsAuthenticated]

    # def get_queryset(self):

    # id_project =  Project.objects.filter(self.kwargs['id'])
    # return Issue.objects.filter(project_id=)

    def get_queryset(self, *args, **kwargs):
        # project_id = [issue.project.id for issue in
        #               Issue.objects.filter(author_user=self.request.user)]
        # return Issue.objects.filter(id__in=project_id)
        return Issue.objects.filter(project=int(self.kwargs['nested_1_pk']))


    def perform_create(self, serializer):
        # project_id = Project.objects.get(
        #     [issue.project.id for issue in Issue.objects.filter(author_user=self.request.user)])
        project =  Project.objects.get(id=int(self.kwargs['nested_1_pk']))
        serializer.save(project=project, author_user=self.request.user)
        # Contributor(user=self.request.user, project=project,
        #             role='AUTHOR').save()
    # def perform_create(self, serializer):
    #     id_project = get_object_or_404(Project, pk=self.kwargs['id'])
    #     serializer.save(project_id=id_project)
    #     # serializer.save(author_user_id=self.request.user)


class CommentViewSet(ModelViewSet):
    serializer_class = CommentsSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self, *args, **kwargs):
        # issue = [comment.issue.id for comment in  # comment.issue.id plutot
        #             Comment.objects.filter(user=self.request.user)]
        # return Issue.objects.filter(id__in=issue)
        return Comment.objects.filter(issue=int(self.kwargs['nested_2_pk']))




    def perform_create(self, serializer):
        # issue = self.kwargs.get('issue')
        # project = Project.objects.get(self.kwargs['id'])
        # id_issue = Issue.objects.filter(project_id=project)
        # serializer.save(issue=id_issue)
        #
        # serializer.save(author_user=self.request.user)
        # Contributor(user=self.request.user, project=project,
        #             role='AUTHOR').save()

        serializer.save(author_user=self.request.user, issue=Issue.objects.get(id=self.kwargs['nested_2_pk']))
#
# class UserViewSet(ViewSet):
#     """
#     A simple ViewSet for listing or retrieving users.
#     """
#
#     def list(self, request):
#         queryset = User.objects.all()
#         serializer = UserSerializer(queryset, many=True)
#         return Response(serializer.data)
#
#     def retrieve(self, request, pk=None):
#         queryset = User.objects.all()
#         user = get_object_or_404(queryset, pk=pk)
#         serializer = UserSerializer(user)
#         return Response(serializer.data)


class ContributorViewSet(ModelViewSet):
    serializer_class = ContributorsSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        id_project = ""
        return Contributor.objects.filter(projet=id_project)
