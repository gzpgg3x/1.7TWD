from django.contrib import admin

# Register your models here.
from myApp.models import Category, Page

admin.site.register(Category)
admin.site.register(Page)