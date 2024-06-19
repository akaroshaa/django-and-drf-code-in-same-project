from django.contrib import admin
from .models import Product, Employee

class ProductAdmin(admin.ModelAdmin):
    list_display = ["id", "product_name", "desc", "pub_date", "price"]

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "address", "doj", "salary"]


admin.site.register(Product, ProductAdmin)
admin.site.register(Employee, EmployeeAdmin)
