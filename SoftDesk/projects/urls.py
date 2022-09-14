from rest_framework_nested import routers
from rest_framework_nested.routers import NestedSimpleRouter
from django.urls import path, include

from projects.views import (
    ProjectViewSet,
    IssueViewSet,
    CommentViewSet,
    ContributorViewSet,
)

router = routers.DefaultRouter()

# /projects/
# /projects/{project_id}
router.register(
    r"projects",
    ProjectViewSet,
    basename="projects",
)

issues_router = NestedSimpleRouter(router, r"projects", "projects")
issues_router.register(r"issues", IssueViewSet, basename="issues")

contributors_router = NestedSimpleRouter(router, r"projects", "projects")
contributors_router.register(r"users",
                             ContributorViewSet,
                             basename="contributors")

comments_router = NestedSimpleRouter(issues_router, r"issues", "issues")
comments_router.register(r"comments", CommentViewSet, basename="comments")

urlpatterns = [
    path("", include(router.urls)),
    path("", include(issues_router.urls)),
    path("", include(comments_router.urls)),
    path("", include(contributors_router.urls)),
]
