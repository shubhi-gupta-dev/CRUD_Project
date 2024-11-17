from django.contrib import admin
from .models import Product

# Register your models here.
@admin.register(Product)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id' , 'pname' , 'pdesc' , 'price' ,'photo']
