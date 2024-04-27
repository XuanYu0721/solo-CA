from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from itsdangerous import URLSafeTimedSerializer as Serializer

class User(AbstractUser):
    groups = models.ManyToManyField('auth.Group', related_name='myuser_groups')
    user_permissions = models.ManyToManyField('auth.Permission', related_name='myuser_permissions')

    def generate_active_token(self):
        serializer = Serializer(settings.SECRET_KEY, 3600) 
        info = {'confirm': self.id}
        token = serializer.dumps(info)
        return token.decode()

        

    class Meta:
        db_table = 'df_user'
        verbose_name = 'User'
        verbose_name_plural = verbose_name


class Address(models.Model):
    user = models.ForeignKey(User, verbose_name='User', related_name='address_user', on_delete=models.CASCADE)
    recipient = models.CharField(max_length=20, verbose_name='Recipient')
    addr = models.CharField(max_length=256, verbose_name='Address') 
    postcode = models.CharField(max_length=6, null=True, verbose_name='Postcode') 
    phone_number = models.CharField(max_length=11, verbose_name='Phone Number')

    class Meta:
        db_table = 'df_address'
        verbose_name = 'Address'
        verbose_name_plural = verbose_name
