from rest_framework import routers
from django.urls import include, path
from .views import VoteViewSet, IdeaViewSet

router = routers.DefaultRouter()
router.register(r'ideas', IdeaViewSet)
router.register(r'votes', VoteViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
