from rest_framework.routers import DefaultRouter
from apps.blog.views import BlogViewSet

router = DefaultRouter()

router.register(r'posts',BlogViewSet, basename='posts')


urlpatterns = router.urls