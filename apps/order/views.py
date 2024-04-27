from django.shortcuts import render
from .models import orderInfo, OrderProduct
from django.contrib.auth.decorators import user_passes_test, permission_required

def order_list(request):
    orders = orderInfo.objects.all().prefetch_related('orderproduct_set')
    return render(request, 'order_list.html', {'orders': orders})

def order_detail(request, order_id):
    order = orderInfo.objects.get(order_id=order_id)
    order_products = OrderProduct.objects.filter(order=order)
    return render(request, 'order_detail.html', {
        'order': order,
        'order_products': order_products
    })

def is_admin(user):
    return user.groups.filter(name='Admin').exists()

@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'admin_page.html', context)

@permission_required('order.can_view_order', raise_exception=True)
def order_view(request):
    return render(request, 'order_page.html', context)