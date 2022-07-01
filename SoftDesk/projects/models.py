from django.conf import settings
from django.db import models


# Create your models here.

class Project(models.Model):
    objects = models.Manager()
    project_id = models.IntegerField()
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=2000)
    type = models.CharField(max_length=200)
    author_user_id = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )


class Contributor(models.Model):
    user_id = models.IntegerField()
    project_id = models.ForeignKey(to=Project, on_delete=models.CASCADE)
    # permission = models.CharField() # voir les choix multiples charfield
    role = models.CharField(max_length=20)


class Issue(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    tag = models.CharField(max_length=200)
    priority = models.CharField(max_length=200)
    project_id = models.ForeignKey(to=Project, on_delete=models.CASCADE)
    status = models.CharField(max_length=200)
    author_user_id = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    assignee_user_id = models.ForeignKey(
        to=Contributor, on_delete=models.CASCADE
    )
    created_time = models.DateTimeField()


class Comment(models.Model):
    comment_id = models.IntegerField()
    description = models.CharField(max_length=2000)
    author_user_id = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    issue_id = models.ForeignKey(
        to=Issue, on_delete=models.CASCADE
    )
    created_time = models.DateTimeField()

# CLASS USER ????
