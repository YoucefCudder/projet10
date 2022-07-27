from rest_framework.serializers import ModelSerializer

from .models import Project, Contributor, Issue, Comment


class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'title', 'description', 'type', 'author_user_id')
        extra_kwargs = {'author_user_id': {'read_only': True}}


class ContributorsSerializer(ModelSerializer):
    class Meta:
        model = Contributor
        fields = ["id", "user_id", "project_id", "role"]


class IssuesSerializer(ModelSerializer):
    class Meta:
        model = Issue
        fields = [
            "id",
            "title",
            "description",
            "tag",
            "priority",
            "project_id",
            "status",
            "author_user_id",
            "assignee_user_id",
            "created_time",
        ]


class CommentsSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ["id", "description", "author_user_id",
                  "issue_id", "created_time"
                  ]
