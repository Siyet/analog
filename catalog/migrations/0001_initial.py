# Generated by Django 2.1.4 on 2019-01-09 03:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Attribute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Когда создано')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Когда обновлено')),
                ('is_public', models.BooleanField(default=True, verbose_name='Опубликовано?')),
                ('deleted', models.BooleanField(default=False, editable=False, verbose_name='В архиве?')),
                ('title', models.CharField(max_length=255, verbose_name='Наименование')),
                ('type', models.CharField(choices=[('hrd', 'Жесткий'), ('sft', 'Мягкий'), ('rcl', 'Пересчет'), ('rlt', 'Взаимосвязь'), ('prc', 'Цена')], max_length=13, verbose_name='Тип')),
                ('unit', models.CharField(blank=True, choices=[('mm', 'мм'), ('cm', 'см'), ('m', 'м'), ('km', 'км'), ('g', 'гр'), ('kg', 'кг'), ('tonne', 'т')], max_length=5, verbose_name='Единицы измерения')),
                ('priority', models.PositiveSmallIntegerField(verbose_name='Приоритет')),
            ],
            options={
                'verbose_name': 'Атрибут',
                'verbose_name_plural': 'Атрибуты',
            },
        ),
        migrations.CreateModel(
            name='AttributeValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Когда создано')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Когда обновлено')),
                ('is_public', models.BooleanField(default=True, verbose_name='Опубликовано?')),
                ('deleted', models.BooleanField(default=False, editable=False, verbose_name='В архиве?')),
                ('title', models.CharField(max_length=255, verbose_name='Значение')),
                ('attribute', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='values', to='catalog.Attribute', verbose_name='Атрибут')),
                ('created_by', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Кем создано')),
            ],
            options={
                'verbose_name': 'Значение атрибута',
                'verbose_name_plural': 'Значения атрибутов',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Когда создано')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Когда обновлено')),
                ('is_public', models.BooleanField(default=True, verbose_name='Опубликовано?')),
                ('deleted', models.BooleanField(default=False, editable=False, verbose_name='В архиве?')),
                ('title', models.CharField(max_length=255, verbose_name='Наименование')),
                ('short_title', models.CharField(blank=True, max_length=255, verbose_name='Краткое наименование')),
                ('created_by', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Кем создано')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='childs', to='catalog.Category', verbose_name='Родительский класс')),
                ('updated_by', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Кем обновлено')),
            ],
            options={
                'verbose_name': 'Класс',
                'verbose_name_plural': 'Классы',
            },
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Когда создано')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Когда обновлено')),
                ('is_public', models.BooleanField(default=True, verbose_name='Опубликовано?')),
                ('deleted', models.BooleanField(default=False, editable=False, verbose_name='В архиве?')),
                ('title', models.CharField(max_length=255, verbose_name='Наименование')),
                ('short_title', models.CharField(blank=True, max_length=255, verbose_name='Краткое наименование')),
                ('created_by', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Кем создано')),
                ('updated_by', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Кем обновлено')),
            ],
            options={
                'verbose_name': 'Производитель',
                'verbose_name_plural': 'Производители',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Когда создано')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Когда обновлено')),
                ('is_public', models.BooleanField(default=True, verbose_name='Опубликовано?')),
                ('deleted', models.BooleanField(default=False, editable=False, verbose_name='В архиве?')),
                ('title', models.CharField(max_length=255, verbose_name='Наименование')),
                ('article', models.CharField(max_length=255, verbose_name='Артикул')),
                ('attrs_vals', models.ManyToManyField(to='catalog.AttributeValue', verbose_name='Атрибуты')),
                ('category', models.ForeignKey(limit_choices_to={'parent__isnull': False}, on_delete=django.db.models.deletion.PROTECT, related_name='products', to='catalog.Category', verbose_name='Класс')),
                ('created_by', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Кем создано')),
                ('manufacturer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='products', to='catalog.Manufacturer', verbose_name='Производитель')),
                ('updated_by', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Кем обновлено')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
        migrations.CreateModel(
            name='Specification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Когда создано')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Когда обновлено')),
                ('is_public', models.BooleanField(default=True, verbose_name='Опубликовано?')),
                ('deleted', models.BooleanField(default=False, editable=False, verbose_name='В архиве?')),
                ('title', models.CharField(max_length=255, verbose_name='Наименование')),
                ('created_by', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Кем создано')),
                ('products', models.ManyToManyField(to='catalog.Product', verbose_name='Товары')),
                ('updated_by', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Кем обновлено')),
            ],
            options={
                'verbose_name': 'Спецификация',
                'verbose_name_plural': 'Спецификации',
            },
        ),
        migrations.AddField(
            model_name='attributevalue',
            name='products',
            field=models.ManyToManyField(to='catalog.Product'),
        ),
        migrations.AddField(
            model_name='attributevalue',
            name='updated_by',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Кем обновлено'),
        ),
        migrations.AddField(
            model_name='attribute',
            name='category',
            field=models.ForeignKey(limit_choices_to={'parent__isnull': False}, on_delete=django.db.models.deletion.PROTECT, related_name='attributes', to='catalog.Category', verbose_name='Класс'),
        ),
        migrations.AddField(
            model_name='attribute',
            name='created_by',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Кем создано'),
        ),
        migrations.AddField(
            model_name='attribute',
            name='updated_by',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Кем обновлено'),
        ),
    ]
