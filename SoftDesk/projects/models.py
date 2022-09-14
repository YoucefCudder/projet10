from django.conf import settings
from django.db import models

# Create your models here.


# tuple binaire pour choix >possible à l'interieur de la classe mais typo diff
# https://docs.djangoproject.com/fr/4.0/ref/models/fields/


class Project(models.Model):
    BACKEND = "BACKEND"
    FRONTEND = "FRONTEND"
    IOS = "IOS"
    ANDROID = "ANDROID"
    TYPES_CHOICES = (
        (BACKEND, "Back-end"),
        (FRONTEND, "Front-end"),
        (IOS, "iOS"),
        (ANDROID, "Android"),
    )
    objects = models.Manager()
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=2000)
    type = models.CharField(max_length=200, choices=TYPES_CHOICES)
    author_user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )


class Contributor(models.Model):
    ROLES = [("AUTHOR", "AUTHOR"), ("CONTRIBUTOR", "CONTRIBUTOR")]
    PERMISSION = [("ALL ACCESS", "ALL ACCESS"), ("RESTRICTED", "RESTRICTED")]
    objects = models.Manager()

    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE)
    project = models.ForeignKey(
        to=Project, on_delete=models.CASCADE, related_name="contributors"
    )
    permission = models.CharField(
        max_length=50, choices=PERMISSION, default="ALL ACCESS"
    )  # voir les choix multiples charfield
    role = models.CharField(max_length=20, choices=ROLES)


class Issue(models.Model):
    STATUS = [("to_do", "to_do"), ("ongoing", "ongoing"), ("done", "done")]
    TAG_CHOICES = [("bug", "bug"), ("upgrade", "upgrade"), ("task", "task")]
    PRIORITY_CHOICES = [("low", "low"), ("Middle", "middle"), ("high", "high")]

    objects = models.Manager()
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    tag = models.CharField(max_length=200, choices=TAG_CHOICES)
    priority = models.CharField(max_length=200, choices=PRIORITY_CHOICES)
    project = models.ForeignKey(to=Project, on_delete=models.CASCADE)
    status = models.CharField(max_length=200, choices=STATUS)
    author_user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    assignee_user = models.ForeignKey(to=Contributor, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    objects = models.Manager()

    description = models.CharField(max_length=2000)
    author_user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    issue = models.ForeignKey(to=Issue, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
