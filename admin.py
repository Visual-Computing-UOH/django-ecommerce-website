
from django.contrib import admin
from .models import Category, Product, Order, OrderItem

admin.site.register(Category)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'name', 'category', 'price', 'old_price',
        'is_best_seller', 'is_new_arrival', 'is_trending', 'is_top_rated', 'is_deal_of_day',
    ]
    list_editable = [
        'is_best_seller', 'is_new_arrival', 'is_trending', 'is_top_rated', 'is_deal_of_day',
    ]
    list_filter = ['category', 'is_best_seller', 'is_new_arrival', 'is_trending', 'is_top_rated', 'is_deal_of_day']
    search_fields = ['name']


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ['product', 'price', 'quantity']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'email', 'phone', 'total_price', 'status', 'created_at']
    list_filter = ['status', 'created_at']
    search_fields = ['full_name', 'email', 'phone']
    inlines = [OrderItemInline]