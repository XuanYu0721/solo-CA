import csv
from django.core.management.base import BaseCommand
from product.models import Product, ProductCategory, ProductBrand

class Command(BaseCommand):
    help = 'Import products data from CSV and load into database'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path to the CSV file containing products')

    def handle(self, *args, **options):
        csv_file_path = options['csv_file']

        # 文件路径是硬编码的，可以直接使用它们，无需os.path.join
        category_csv_file = '/home/codio/workspace/solo-assessment/ecommerce_data/product_categories.csv'
        brand_csv_file = '/home/codio/workspace/solo-assessment/ecommerce_data/product_brands.csv'
        product_csv_file = '/home/codio/workspace/solo-assessment/ecommerce_data/product.csv'  # 确保文件名正确

        # 先加载类别和品牌到数据库
        with open(category_csv_file, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                ProductCategory.objects.get_or_create(name=row['category_name'])

        with open(brand_csv_file, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                ProductBrand.objects.get_or_create(name=row['brand_name'])

        # 加载产品
        with open(product_csv_file, 'r', encoding='ISO-8859-1') as file:
            reader = csv.DictReader(file)
            for row in reader:
                category, created = ProductCategory.objects.get_or_create(name=row['category_name'])
                brand, created = ProductBrand.objects.get_or_create(name=row['brand_name'])

                # 创建产品实例
                product = Product(
                    name=row['product_name'],
                    ingredient=row['ingredients'],
                    price=row['price'],
                    category=category,
                    brand=brand,
                    # ... 其他字段
                )
                product.save()

        self.stdout.write(self.style.SUCCESS('Successfully imported products'))
