from django.db import models
from django.utils import timezone

class ProductCategory(models.Model):
    name = models.CharField(max_length=20, verbose_name='Product category name')
    
    class Meta:
        db_table = 'df_product_category'
        verbose_name = 'Product category'
        verbose_name_plural = verbose_name
        app_label = 'product'
    
    def __str__(self):
        return self.name

class ProductBrand(models.Model):
    name = models.CharField(max_length=20, verbose_name='Brand name')

    class Meta:
        db_table = 'df_brand'
        verbose_name = 'Brand'
        verbose_name_plural = verbose_name
        app_label = 'product'

    def __str__(self):
        return self.name

class Product(models.Model):

    category = models.ForeignKey('ProductCategory', verbose_name='Product category', on_delete=models.CASCADE)
    brand = models.ForeignKey('ProductBrand', verbose_name='Product brand', on_delete=models.CASCADE)
    name = models.CharField(max_length=20, verbose_name='Product name')
    ingredient = models.CharField(max_length=256, verbose_name='Product ingredient')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Price')
    image = models.ImageField(upload_to='product', verbose_name='Product picture')
    
    created_at = models.DateTimeField(default=timezone.now, verbose_name='Created at')
    updated_at = models.DateTimeField(default=timezone.now, verbose_name='Updated at')

    class Meta:
        db_table = 'df_product'
        verbose_name = 'Product'
        verbose_name_plural = verbose_name
        app_label = 'product'
    
    def save(self, *args, **kwargs):
        # 更新时自动设置 updated_at 字段
        if not self._state.adding:
            self.updated_at = timezone.now()
        super(Product, self).save(*args, **kwargs)

class IndexProductBanner(models.Model):
    product = models.ForeignKey('Product', verbose_name='Product', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='banner', verbose_name='Picture') 
    index = models.SmallIntegerField(default=0, verbose_name='Display order')
    
    class Meta:
        db_table = 'df_index_banner'
        verbose_name ='Homepage display product'
        verbose_name_plural = verbose_name
        app_label = 'product'

