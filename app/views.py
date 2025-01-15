from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView
from .models import Product, Checkout, Inventory
from .serializers import ProductSerializer, CheckoutSerializer, InventorySerializer
from .producer import publish_task


class ProductApiView(ListAPIView, CreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def perform_create(self, serializer):
        product = serializer.save()
        message = {
            "action": "product_added",
            "item_name": product.name,
            "quantity": product.quantity,
        }
        publish_task(message)


class InventoryApiView(ListAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer


class InventoryDetailApiView(RetrieveAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
    lookup_field = "name"
    # lookup_field = 'pk'


class CheckoutApiView(ListAPIView, CreateAPIView):
    serializer_class = CheckoutSerializer
    queryset = Checkout.objects.select_related("name").all()

    def perform_create(self, serializer):
        product = serializer.save()
        message = {
            "action": "product_checked_out",
            "item_name": product.name.name,
            "quantity": product.quantity,
        }
        publish_task(message)
