import csv
from models import orderInfo, OrderProduct, User, Address, Product

def parse_orders_csv(file_path):
    with open(file_path, mode='r', encoding='utf-8') as csvfile:
        order_reader = csv.reader(csvfile)
        for row in order_reader:
            user = User.objects.get(id=row[1])  # Assuming the user ID is the second column
            address = Address.objects.get(id=row[2])  # Assuming the address ID is the third column
            product = Product.objects.get(id=row[7])  # Assuming the product ID is the eighth column

            # Create the orderInfo
            order = orderInfo.objects.create(
                order_id=row[0],
                user=user,
                addr=address,
                pay_method=row[3],
                total_quantity=row[4],
                total_price=row[5],
                shipping_fee=row[6],
                order_status=row[7]
            )

            # Create the OrderProduct
            OrderProduct.objects.create(
                order=order,
                product=product,
                quantity=row[8],
                price=row[9],
                review=row[10] if len(row) > 10 else ''
            )

# Replace 'your_orders.csv' with the path to your CSV file.
parse_orders_csv('your_orders.csv')
