from django.contrib import admin

from .models import Category, Subcategory, Product, Manufacturer, Attribute, AttributeValue, Specification, Listing

class BaseAdmin(admin.ModelAdmin):
    
    def save_model(self, request, obj, form, change): 
        if not change:
            obj.created_by = request.user
        obj.updated_by = request.user
        obj.save()

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        for instance in instances:
            instance.updated_by = request.user
            instance.save()


class CategoryAdmin(BaseAdmin):
    list_display=['title','id','rev','is_public','deleted','created_at','created_by','updated_at','updated_by']

# class ListingAdmin(BaseAdmin):
#     actions = None
#     search_fields = ['=user__username', ]
#     fieldsets = [
#         (None, {'fields':()}), 
#         ]

#     def __init__(self, *args, **kwargs):
#         super(LogEntryAdmin, self).__init__(*args, **kwargs)
#         self.list_display_links = (None, )

# TODO реализовать фильтры поиска по колонкам, рецепт тут: https://medium.com/@hakibenita/how-to-add-a-text-filter-to-django-admin-5d1db93772d8 
# TODO экспорт в формат xls https://xlsxwriter.readthedocs.io/index.html 

admin.site.register(Category, CategoryAdmin)
admin.site.register(Subcategory, BaseAdmin)
admin.site.register(Product, BaseAdmin)
admin.site.register(Manufacturer, BaseAdmin)
admin.site.register(Attribute, BaseAdmin)
admin.site.register(Specification, BaseAdmin)
admin.site.register(Listing, BaseAdmin)

# Register your models here.
