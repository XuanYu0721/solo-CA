from django.db import models
from django.conf import settings
# Create your models here.

class orderInfo(models.Model):
    PAY_METHOD_CHOICES = (
        (1, 'Apple pay'),
        (2, 'Credit or debit card'),
        (3, 'Gift card'),
        (4, 'PayPal'),
    )
    
    ORDER_STATUS_CHOICES =(
        (1, 'Pending'),
        (2, 'Shipped'),
        (3, 'Delivered'),
        (4, 'Cancelled'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='User', on_delete=models.CASCADE)
    addr = models.ForeignKey('user.Address', verbose_name='Address', on_delete=models.CASCADE)
    pay_method = models.SmallIntegerField(choices=PAY_METHOD_CHOICES, default=3, verbose_name='Payment method')
    total_quantity = models.IntegerField(default=1, verbose_name='Total quantity')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Total Price')
    shipping_fee = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Shipping fee')
    order_status = models.SmallIntegerField(choices=ORDER_STATUS_CHOICES, default=1, verbose_name='Order status')

    class Meta:
        db_table = 'df_order_info'
        app_label = 'order'

class OrderProduct(models.Model):
    order = models.ForeignKey('OrderInfo', verbose_name='Order', on_delete=models.CASCADE)
    product = models. ForeignKey('product.Product', verbose_name='Product', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1, verbose_name='Quantity')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Price')
    review = models.CharField(max_length=256, verbose_name='Review')
    
    class Meta:
        db_table = 'df_order_product'