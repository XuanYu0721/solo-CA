"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from product.views import home, search_view, search_results
from django.conf.urls import handler404, handler500


urlpatterns = [
    path('admin/', admin.site.urls),
    path('cart/', include('apps.cart.urls')),
    path('order/', include('apps.order.urls')),
    path('product/', include('apps.product.urls')),
    path('user/', include('apps.user.urls')),
    path('', home, name='home'), 
    path('search/', search_view, name='search'),
    path('search/results/', search_results, name='search_results'),
]

handler404 = 'apps.product.views.custom_404'
handler500 = 'apps.product.views.custom_500'
