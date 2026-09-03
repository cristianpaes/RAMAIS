from rest_framework.routers import DefaultRouter

from app.views import ramaisViewSet


router = DefaultRouter()

router.register(
    r"",
    ramaisViewSet,
    basename="ramais"
)

urlpatterns = router.urls