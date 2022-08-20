from rest_framework import routers
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers
from rest_framework_nested.routers import NestedSimpleRouter

from projects import views
from django.urls import path, include

from projects.views import ProjectViewSet, IssueViewSet, CommentViewSet, \
    ContributorViewSet

router = routers.DefaultRouter()

# /projects/
# /projects/{project_id}
router.register(
    r'projects',
    ProjectViewSet,
    basename='projects',
)

issues_router = NestedSimpleRouter(router, r'projects', 'projects')
issues_router.register(r'issues', IssueViewSet, basename='issues')

contributors_router = NestedSimpleRouter(router, r'projects', 'projects')
contributors_router.register(r'users', ContributorViewSet, basename='contributors')


comments_router = NestedSimpleRouter(issues_router, r'issues', 'issues')
comments_router.register(r'comments', CommentViewSet, basename='comments')



# /projects/{project_id}/issues/
# /projects/{project_id}/issues/{issue_id}/
# router.register(r'projects/(?P<project_id>[^/.]+)/issues', IssueViewSet, basename='issues')

#
# router.register(
#     r'projects/(?P<project_id>[^/.]+)/issues/(?P<issue_id>[^/.]+)/comments', CommentViewSet,basename='comments')
#
# # router.register(r"^(?P<project_id>[^/.]+)/issues/(?P<issue_id>[^/.]+)/comments", CommentViewSet, basename="comments")
# # router = routers.SimpleRouter()
# # router.register('projects', ProjectViewSet, basename='projects')
# router.register('projects/<int:pk>', ProjectViewSet, basename='detail')
# router.register('projects/<int:pk>/issues', IssueViewSet, basename="issues")
#router.register('projects/<int:id>', ProjectViewSet, basename='detail')
# issue_router = routers.NestedSimpleRouter(router, r'projects', lookup='projects')
# issue_router.register(r"issues", IssueViewSet,
#                        basename='issue')
# router.register(r"^(?P<id>[^/.]+)/issues/(?P<issue_id>[^/.]+)/comments", CommentsViewSet, basename="comments")

urlpatterns = [
    path('', include(router.urls)),
    path('', include(issues_router.urls)),
    path('', include(comments_router.urls)),
    path('', include(contributors_router.urls)),

    # path('projects/<uuid:pk>/issues', IssueViewSet.as_view({'post': 'create'}))

]
