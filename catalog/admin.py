from django.contrib import admin

from .models import Category, Subcategory, Product, Manufacturer, Attribute, AttributeValue, Specification, Listing

admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Product)
admin.site.register(Manufacturer)
admin.site.register(Attribute)
admin.site.register(Specification)
admin.site.register(Listing)

# Register your models here.
