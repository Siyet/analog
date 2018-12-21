from django.contrib import admin

from .models import Category, Subcategory, Product, Manufacturer, Attribute, AttributeValue, Specification

def mark_as_published(modeladmin, request, queryset):
    queryset.update(is_public=True)
mark_as_published.short_description = u"Опубликовать"

def mark_as_unpublished(modeladmin, request, queryset):
    queryset.update(is_public=False)
mark_as_unpublished.short_description = u"Снять с публикации"


class BaseAdmin(admin.ModelAdmin):

    list_display = ['uid','title', 'is_public', 'deleted','created_at','created_by','updated_at','updated_by']
    save_on_top = True
    actions = [mark_as_published, mark_as_unpublished]
    list_filter = ['is_public', 'deleted','created_at','updated_at']
    
    def save_model(self, request, obj, form, change): 
        if not change:
            obj.created_by = request.user
        obj.updated_by = request.user
        obj.save()

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        for instance in instances:
            if not change:
                instance.created_by = request.user
            instance.updated_by = request.user
            instance.save()


class SubCatValInline(admin.TabularInline):
    model = Subcategory


class CategoryAdmin(BaseAdmin):
    inlines=[SubCatValInline]


class AttrAdmin(BaseAdmin):
    list_display=['uid','title', 'type', 'priority','subcategory','is_public', 'deleted']


class AttrValInline(admin.TabularInline):
    model = AttributeValue


class ProductAdmin(BaseAdmin):
    list_display=['uid','article', 'manufacturer', 'subcategory','is_public', 'deleted']
    inlines = [AttrValInline]

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
admin.site.register(Product, ProductAdmin)
admin.site.register(Manufacturer, BaseAdmin)
admin.site.register(Attribute, AttrAdmin)
admin.site.register(Specification, BaseAdmin)

# Register your models here.
