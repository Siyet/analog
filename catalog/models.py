"""
Описание основных моделей проекта
"""

from django.db import models
import uuid
from django.contrib.auth.models import User
from django.utils import timezone


class Base(models.Model):
    """
    Абстрактная базовая модель
    """
    uid = models.UUIDField(verbose_name="Идентификатор", primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Когда создано")
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name="Кем создано", editable=False, related_name="+")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Когда обновлено")
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name="Кем обновлено", editable=False, related_name="+")
    is_public = models.BooleanField("Опубликовано?", default=True)
    deleted = models.BooleanField("В архиве?", default=False, editable=False)
    rev = models.CharField("Ревизия", default='1-{0}'.format(uuid.uuid4()), max_length=38, editable=False)
    # json-delta пакет для работы с разностью в json; json_patch - функция пакета для применения изменений.

    class Meta:
        abstract = True
        verbose_name = "Базовая модель "
        verbose_name_plural = "Базовые модели"

    # def save(self, *args, **kwargs):
    #     if not self.uid:
    #         self.created_at = timezone.now()
        
    #     self.updated_at = timezone.now()
    #     return super(Base, self).save(*args, **kwargs)


class Manufacturer(Base):
    """
    Модель производителя товаров
    """
    title = models.CharField(verbose_name='Наименование', max_length=255)
    short_title = models.CharField(verbose_name='Краткое наименование', max_length=255, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Производитель"
        verbose_name_plural = "Производители"


class Category(Base):
    """
    Модель класса товаров
    """
    subcategories = None
    title = models.CharField(max_length=255, verbose_name='Наименование')
    short_title = models.CharField(max_length=255, verbose_name='Краткое наименование', blank=True)
    
    def getAttributes(self):
        if not self.subcategories:
            return []
        attrs = []
        for subcat in self.subcategories.all():
            _attrs = subcat.attributes if subcat.attributes else []
            diff = set(attrs) - set(_attrs)
            attrs = attrs + list(diff)
        return attrs

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Класс"
        verbose_name_plural = "Классы"


class Subcategory(Base):
    """
    Модель вида (подкласса) товаров
    """
    title = models.CharField(max_length=255, verbose_name='Наименование')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name="Класс", related_name='subcategories')
    short_title = models.CharField(max_length=255, verbose_name='Краткое наименование', blank=True)
    
    def __str__(self):
        return self.category.title + ' -> ' + self.title

    class Meta:
        verbose_name = "Подкласс"
        verbose_name_plural = "Подклассы"


class Attribute(Base):
    """
    Модель атрибута товара
    """
    HARD          = 'hrd'
    SOFT          = 'sft'
    RECALCULATION = 'rcl'
    RELATION      = 'rlt'
    PRICE         = 'prc'
    TYPES = (
        (HARD,          'Жесткий'),
        (SOFT,          'Мягкий'),
        (RECALCULATION, 'Пересчет'),
        (RELATION,      'Взаимосвязь'),
        (PRICE,         'Цена')
    )

    title = models.CharField(max_length=255, verbose_name='Наименование')
    type = models.CharField(max_length=13, choices=TYPES, verbose_name="Тип")
    priority = models.PositiveSmallIntegerField(verbose_name='Приоритет')
    subcategory = models.ForeignKey(Subcategory, on_delete=models.PROTECT, verbose_name="Подкласс", related_name='attributes')
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Атрибут"
        verbose_name_plural = "Атрибуты"


class Product(Base):
    """
    Модель товара
    """
    article = models.CharField(max_length=255, verbose_name='Артикул')
    subcategory = models.ForeignKey(Subcategory, on_delete=models.PROTECT, verbose_name="Вид", related_name='products')
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.PROTECT, verbose_name="Производитель", related_name='products')

    def __str__(self):
        return self.article

    def title(self):
        return self.article

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"


class AttributeValue(Base):
    """
    Модель значения атрибута
    """
    title = models.CharField(max_length=255, verbose_name='Значение')
    attribute = models.ForeignKey(Attribute, on_delete=models.PROTECT, verbose_name="Атрибут", related_name="values")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Атрибуты", related_name="attrs_values")

    class Meta:
        verbose_name = "Значение атрибута"
        verbose_name_plural = "Значения атрибутов"


class Specification(Base):
    """
    Модель спецификации предложений товаров
    """
    title = models.CharField(max_length=255, verbose_name='Наименование')
    products = models.ManyToManyField(Product, verbose_name="Товары")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Спецификация"
        verbose_name_plural = "Спецификации"