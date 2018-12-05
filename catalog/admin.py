from django.contrib import admin

from .models import Category, Subcategory, Product, Manufacturer, Attribute, AttributeValue, Specification, Listing

class BaseAdmin(admin.ModelAdmin):
    def save_model(self, request, instance, form, change):
        user = request.user 
        instance = form.save(commit=False)
        if not change or not instance.created_by:
            instance.created_by = user
        instance.updated_by = user
        instance.save()
        form.save_m2m()
        return instance

admin.site.register(Category, BaseAdmin)
admin.site.register(Subcategory, BaseAdmin)
admin.site.register(Product, BaseAdmin)
admin.site.register(Manufacturer, BaseAdmin)
admin.site.register(Attribute, BaseAdmin)
admin.site.register(Specification, BaseAdmin)
admin.site.register(Listing, BaseAdmin)

# Register your models here.
