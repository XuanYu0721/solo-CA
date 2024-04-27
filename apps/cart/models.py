from django.db import models
from django.conf import settings

class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='cart')
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Cart'
        verbose_name_plural = 'Carts'
        app_label = 'cart'

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    class Meta:
        verbose_name = 'Cart Item'
        verbose_name_plural = 'Cart Items'
