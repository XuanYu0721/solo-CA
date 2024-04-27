# cart/parse_csv.py
import csv
from django.contrib.auth import get_user_model
from product.models import Product
from .models import CartItem
from datetime import datetime

User = get_user_model()

def parse_csv(file_path):
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            user = User.objects.get(username=row['username'])
            product = Product.objects.get(name=row['product_name'])
            date_added = datetime.strptime(row['date_added'], '%d-%m-%Y').date()
            CartItem.objects.create(
                user=user,
                product=product,
                quantity=int(row['quantity']),
                date_added=date_added
            )

# Replace 'your_cart.csv' with the path to your actual CSV file.
# parse_csv('your_cart.csv')
