from rest_framework.routers import DefaultRouter
from product.api import views

app_name = "product"
router = DefaultRouter()

router.register(r'product', views.ProductViewSet)

urlpatterns = router.urls