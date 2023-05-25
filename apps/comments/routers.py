from rest_framework.routers import DefaultRouter
from .views import CommentsViewSet

router = DefaultRouter()

router.register('comments', CommentsViewSet, basename= 'comments')

urlpatterns= router.urls