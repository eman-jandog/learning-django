from django.urls import path
from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()
router.register('products', views.ProductViewSet)
router.register('collections', views.CollectionViewSet)
router.register('carts', views.CartViewSet)
router.register('customers', views.CustomerViewset)
router.register('orders', views.OrderViewSet, basename='orders')

products_router = routers.NestedDefaultRouter(router, 'products', lookup='product')
products_router.register('reviews', views.ReviewViewSet, basename='product-reviews')
carts_router = routers.NestedDefaultRouter(router, 'carts', lookup='cart')
carts_router.register('items', views.CartItemViewSet, basename= "carts-item-detail")

urlpatterns = router.urls + products_router.urls + carts_router.urls