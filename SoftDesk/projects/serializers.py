from rest_framework.serializers import ModelSerializer

from .models import Project, Contributor, Issue, Comment


class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = ("id", "title", "description", "type")
        extra_kwargs = {"author_user": {"read_only": True}}


class ProjectDetailSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"


class ContributorsSerializer(ModelSerializer):
    class Meta:
        model = Contributor
        fields = ["id", "user", "role", "permission"]
        extra_kwargs = {"project": {"read_only": True}}


class IssueSerializer(ModelSerializer):
    class Meta:
        model = Issue
        fields = [
            "id",
            "title",
            "description",
            "tag",
            "priority",
            "project",
            "status",
            "author_user",
            "assignee_user",
        ]
        extra_kwargs = {"created_time": {"read_only": True}}


class CommentsSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ["id", "description", "author_user", "issue", "created_time"]
