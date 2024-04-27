# cart/views.py
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from .models import CartItem
from product.models import Product
from django.contrib import messages

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = CartItem.objects.get_or_create(
        user=request.user,
        product=product,
        defaults={'quantity': 1} 
    )
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    messages.success(request, "Product added to cart.")
    return redirect('product_list') 
@login_required
def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id, user=request.user)
    cart_item.delete()
    messages.success(request, "Product removed from cart.")
    return redirect('cart_detail')  
