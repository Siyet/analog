"""
Описание основных моделей проекта
"""

from django.db import models
import uuid
from django.contrib.auth.models import User

def getUuid():
    return str(uuid.uuid4()).replace('-','')


class Base(models.Model):
    """
    Абстрактная базовая модель
    """

    id = models.UUIDField(primary_key=True, default=getUuid(), editable=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Когда создано", editable=False)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name="Кем создано", editable=False, related_name="+")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Когда обновлено", editable=False)
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name="Кем обновлено", editable=False, related_name="+")
    is_public = models.BooleanField("Опубликовано?", default=False)
    deleted = models.BooleanField("Удалено?", default=False, editable=False)
    rev = models.CharField("Ревизия", default='1-{0}'.format(getUuid()), max_length=64, editable=False)

    class Meta:
        abstract = True
        verbose_name = "Базовая модель"
        verbose_name_plural = "Базовые модели"


class Product(Base):
    """
    Модель товара
    """
    
    title = models.CharField(max_length=255, verbose_name='Наименование')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name="Класс", related_name='products')
    subcategory = models.ForeignKey('Subcategory', on_delete=models.PROTECT, verbose_name="Вид", related_name='products')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

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
    priority = models.PositiveSmallIntegerField
    subcategory = models.ForeignKey('Subcategory', on_delete=models.PROTECT, verbose_name="Вид (подкласс)", related_name='attributes')
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Атрибут"
        verbose_name_plural = "Атрибуты"

    
class AttributeValue(Base):
    """
    Модель значения атрибута
    """
    title = models.CharField(max_length=255, verbose_name='Наименование')
    attribute = models.ForeignKey(Attribute, on_delete=models.PROTECT, verbose_name="Атрибут", related_name="values")

    class Meta:
        verbose_name = "Значение атрибута"
        verbose_name_plural = "Значения атрибутов"


class Specification(Base):
    """
    Модель спецификации предложений товаров
    """
    
    title = models.CharField(max_length=255, verbose_name='Наименование')

    class Meta:
        verbose_name = "Спецификация"
        verbose_name_plural = "Спецификации"


class Listing(Base):
    """
    Модель предложения/позиции товара
    """

    manufacturer = models.ForeignKey('Manufacturer', on_delete=models.PROTECT, verbose_name="Производитель", related_name='listings')
    product = models.ForeignKey('Product', on_delete=models.PROTECT, verbose_name="Товар", related_name="listings")
    article = models.CharField(max_length=64, verbose_name="Артикул")
    
    def __str__(self):
        return '{0} ({1})'.format(self.product.title, self.manufacturer.title)

    class Meta:
        verbose_name = "Позиция (предложение)"
        verbose_name_plural = "Позиции (предложения)"
    

class Category(Base):
    """
    Модель класса товаров
    """

    subcategories = None

    title = models.CharField(max_length=255, verbose_name='Наименование')
    synonyms = models.CharField(max_length=255, verbose_name='Синонимы', help_text="Вписывайте синонимы через точку с запятой")
    
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
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Вид (подкласс)"
        verbose_name_plural = "Виды (подклассы)"

class Manufacturer(Base):
    """
    Модель производителя товаров
    """

    title = models.CharField(max_length=255, verbose_name='Наименование')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Производитель"
        verbose_name_plural = "Производители"