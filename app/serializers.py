from rest_framework.serializers import ModelSerializer, CharField, ValidationError
from .models import Product, Checkout, Inventory


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class InventorySerializer(ModelSerializer):
    class Meta:
        model = Inventory
        fields = "__all__"


class CheckoutSerializer(ModelSerializer):
    name = CharField()

    class Meta:
        model = Checkout
        fields = "__all__"

    def validate(self, attrs):

        try:
            item = attrs["name"]
            item_obj = Inventory.objects.get(name=item)
        except Inventory.DoesNotExist:
            raise ValidationError({"name": "Item not found"})

        requested_quantity = attrs["quantity"]

        if requested_quantity > item_obj.quantity or item_obj.quantity == 0:
            raise ValidationError(
                {
                    "error": f"Requested quantity ({requested_quantity}) exceeds, available stock ({item_obj.quantity})."
                }
            )
        else:
            attrs["name"] = item_obj
            return attrs
