from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CartViewSet

# Router for /api/cart/items/ endpoint
items_router = DefaultRouter()
items_router.register(r'items', CartViewSet, basename='cart-items')

urlpatterns = [
    # /api/cart/items/ - list and create cart items
    path('', include(items_router.urls)),
]
