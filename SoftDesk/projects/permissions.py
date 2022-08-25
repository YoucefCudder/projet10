from rest_framework import permissions

from projects.models import Contributor, Project


class ProjectPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return True
        # return super().has_permission(request, view)

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS and Contributor.objects\
                .filter(project=obj)\
                .filter(user=request.user):
            return True

        # Instance must have an attribute named `owner`.
        return obj.author_user == request.user


class IssuePermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if Contributor.objects.filter(
                project=view.kwargs['nested_1_pk']).filter(user=request.user):
            return True
        return False

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Instance must have an attribute named `owner`.
        return obj.author_user == request.user


class CommentPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if Contributor.objects.filter(
                project=view.kwargs['nested_1_pk']).filter(user=request.user):
            return True
        return False

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Instance must have an attribute named `owner`.
        return obj.author_user == request.user


class ContributorPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        # all http requests
        if Contributor.objects.filter(
                project=view.kwargs['nested_1_pk']).filter(user=request.user):
            return True
        return False

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Instance must have an attribute named `owner`.
        return obj.author_user == request.user
