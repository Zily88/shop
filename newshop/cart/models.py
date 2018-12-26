from django.db import models
from django.conf import settings
from mainapp.models import ProductItem

# Create your models here.

class CartProduct(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductItem, on_delete=models.CASCADE)
    add_datetime = models.DateTimeField(auto_now_add=True)

    def get_price(self):
        all_products = CartProduct.objects.filter(user=self.user)
        cost = 0
        for item in all_products:
            cost += item.product.price
        return cost

    def get_quantity(self):
        all_products = CartProduct.objects.filter(user=self.user)
        quantity = len(all_products)
        return quantity