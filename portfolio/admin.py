from django.contrib import admin
from .models import Product
from .models import Profile

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price")
    search_fields = ("name",)

admin.site.register(Product, ProductAdmin,)
admin.site.register(Profile)

