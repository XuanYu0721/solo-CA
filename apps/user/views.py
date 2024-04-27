from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# apps/user/views.py
def add_to_user(request):
    return HttpResponse("Item added to user")

def remove_from_user(request):
    return HttpResponse("Item removed from user")
