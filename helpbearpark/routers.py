from rest_framework import routers
from posts.viewsets import TaskViewSet, UserViewSet, ContactViewSet

router = routers.DefaultRouter()

router.register(r'task', TaskViewSet)
router.register(r'user', UserViewSet)
router.register(r'contact', ContactViewSet)