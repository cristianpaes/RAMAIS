from app.views import ramaisViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', ramaisViewSet)

urlpatterns = router.urls