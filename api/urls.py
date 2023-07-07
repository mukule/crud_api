from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import StockViewSet, PriceViewSet, OrderViewSet

router = DefaultRouter()
router.register('stock', StockViewSet)
router.register('price', PriceViewSet)
router.register('order', OrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
