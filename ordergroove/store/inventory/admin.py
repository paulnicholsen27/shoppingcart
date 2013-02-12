from django.contrib import admin
from inventory.models import Product, Category, Store

class CategoryAdmin(admin.ModelAdmin):
	list_display = ('name', 'created_at', 'updated_at',)
	list_display_links = ('name',)
	list_per_page = 20
	ordering = ['name']
	search_fields = ('name', 'description')

admin.site.register(Category)

class ProductAdmin(admin.ModelAdmin):
	list_display = ('name', 'price', 'old_price', 'created_at', 'updated_at',)
	list_display_links = ('name',)
	list_per_page = 50
	ordering = ['-created_at']
	search_fields = ('name', 'description')

admin.site.register(Product,)

class StoreAdmin(admin.ModelAdmin):
	list_display = ('name', 'email',)
	list_display_links = ('name',)
	list_per_page = 10
	ordering = ['name']
	search_fields = ('name', 'email', 'city', 'state')

admin.site.register(Store,)