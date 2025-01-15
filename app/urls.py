from django.urls import path


from .views import ProductApiView, CheckoutApiView, InventoryApiView, InventoryDetailApiView

urlpatterns = [
    path("products/", ProductApiView.as_view()),
    path("checkout/", CheckoutApiView.as_view()),
    path("inventory/", InventoryApiView.as_view()),
    path("inventory/<str:name>", InventoryDetailApiView.as_view()),
    # path("inventory/<pk>", InventoryDetailApiView.as_view()),
]
