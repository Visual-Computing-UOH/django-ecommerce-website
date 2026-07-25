import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings')
django.setup()

from store.models import Category

categories = [
    ("Men's Fashion", "Shirts, jackets, formal and casual wear for men."),
    ("Women's Fashion", "Dresses, frocks, western and eastern wear for women."),
    ("Electronics", "Laptops, cameras, tablets, headphones and gadgets."),
    ("Jewellery", "Necklaces, earrings, rings, bangles and bracelets."),
    ("Footwear", "Sports, formal, casual and party wear shoes."),
    ("Cosmetics", "Skincare, makeup kits, perfumes and beauty essentials."),
    ("Perfume", "Colognes, deodorants and fragrance collections."),
    ("Bags and Accessories", "Handbags, wallets, backpacks and travel bags."),
]

for name, desc in categories:
    Category.objects.get_or_create(name=name, defaults={"description": desc})

print("Done:", Category.objects.count())