# Generated by Django 2.1.3 on 2018-11-29 02:22

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
                ('id', models.UUIDField(default='a33735368cf645158330ab1d985e0ced', editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Когда создано')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Когда обновлено')),
                ('is_public', models.BooleanField(default=False, verbose_name='Опубликовано?')),
                ('deleted', models.BooleanField(default=False, editable=False, verbose_name='Удалено?')),
                ('rev', models.CharField(default='1-e3ecb7b65c3d4068b286a5f2cb4c8afc', editable=False, max_length=64, verbose_name='Ревизия')),
                ('title', models.CharField(max_length=255, verbose_name='Наименование')),
                ('type', models.CharField(choices=[('hrd', 'Жесткий'), ('sft', 'Мягкий'), ('rcl', 'Пересчет'), ('rlt', 'Взаимосвязь'), ('prc', 'Цена')], max_length=13, verbose_name='Тип')),
                ('created_by', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Кем создано')),
            ],
            options={
                'verbose_name': 'Атрибут',
                'verbose_name_plural': 'Атрибуты',
            },
        ),
        migrations.CreateModel(
            name='AttributeValue',
            fields=[
                ('id', models.UUIDField(default='a33735368cf645158330ab1d985e0ced', editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Когда создано')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Когда обновлено')),
                ('is_public', models.BooleanField(default=False, verbose_name='Опубликовано?')),
                ('deleted', models.BooleanField(default=False, editable=False, verbose_name='Удалено?')),
                ('rev', models.CharField(default='1-e3ecb7b65c3d4068b286a5f2cb4c8afc', editable=False, max_length=64, verbose_name='Ревизия')),
                ('title', models.CharField(max_length=255, verbose_name='Наименование')),
                ('attribute', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='values', to='catalog.Attribute', verbose_name='Атрибут')),
                ('created_by', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Кем создано')),
                ('updated_by', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Кем обновлено')),
            ],
            options={
                'verbose_name': 'Значение атрибута',
                'verbose_name_plural': 'Значения атрибутов',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.UUIDField(default='a33735368cf645158330ab1d985e0ced', editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Когда создано')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Когда обновлено')),
                ('is_public', models.BooleanField(default=False, verbose_name='Опубликовано?')),
                ('deleted', models.BooleanField(default=False, editable=False, verbose_name='Удалено?')),
                ('rev', models.CharField(default='1-e3ecb7b65c3d4068b286a5f2cb4c8afc', editable=False, max_length=64, verbose_name='Ревизия')),
                ('title', models.CharField(max_length=255, verbose_name='Наименование')),
                ('created_by', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Кем создано')),
                ('updated_by', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Кем обновлено')),
            ],
            options={
                'verbose_name': 'Класс',
                'verbose_name_plural': 'Классы',
            },
        ),
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.UUIDField(default='a33735368cf645158330ab1d985e0ced', editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Когда создано')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Когда обновлено')),
                ('is_public', models.BooleanField(default=False, verbose_name='Опубликовано?')),
                ('deleted', models.BooleanField(default=False, editable=False, verbose_name='Удалено?')),
                ('rev', models.CharField(default='1-e3ecb7b65c3d4068b286a5f2cb4c8afc', editable=False, max_length=64, verbose_name='Ревизия')),
                ('article', models.CharField(max_length=64, verbose_name='Артикул')),
                ('created_by', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Кем создано')),
            ],
            options={
                'verbose_name': 'Позиция (предложение)',
                'verbose_name_plural': 'Позиции (предложения)',
            },
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.UUIDField(default='a33735368cf645158330ab1d985e0ced', editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Когда создано')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Когда обновлено')),
                ('is_public', models.BooleanField(default=False, verbose_name='Опубликовано?')),
                ('deleted', models.BooleanField(default=False, editable=False, verbose_name='Удалено?')),
                ('rev', models.CharField(default='1-e3ecb7b65c3d4068b286a5f2cb4c8afc', editable=False, max_length=64, verbose_name='Ревизия')),
                ('title', models.CharField(max_length=255, verbose_name='Наименование')),
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
                ('id', models.UUIDField(default='a33735368cf645158330ab1d985e0ced', editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Когда создано')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Когда обновлено')),
                ('is_public', models.BooleanField(default=False, verbose_name='Опубликовано?')),
                ('deleted', models.BooleanField(default=False, editable=False, verbose_name='Удалено?')),
                ('rev', models.CharField(default='1-e3ecb7b65c3d4068b286a5f2cb4c8afc', editable=False, max_length=64, verbose_name='Ревизия')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='products', to='catalog.Category', verbose_name='Класс')),
                ('created_by', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Кем создано')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
        migrations.CreateModel(
            name='Specification',
            fields=[
                ('id', models.UUIDField(default='a33735368cf645158330ab1d985e0ced', editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Когда создано')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Когда обновлено')),
                ('is_public', models.BooleanField(default=False, verbose_name='Опубликовано?')),
                ('deleted', models.BooleanField(default=False, editable=False, verbose_name='Удалено?')),
                ('rev', models.CharField(default='1-e3ecb7b65c3d4068b286a5f2cb4c8afc', editable=False, max_length=64, verbose_name='Ревизия')),
                ('title', models.CharField(max_length=255, verbose_name='Наименование')),
                ('created_by', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Кем создано')),
                ('updated_by', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Кем обновлено')),
            ],
            options={
                'verbose_name': 'Спецификация',
                'verbose_name_plural': 'Спецификации',
            },
        ),
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('id', models.UUIDField(default='a33735368cf645158330ab1d985e0ced', editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Когда создано')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Когда обновлено')),
                ('is_public', models.BooleanField(default=False, verbose_name='Опубликовано?')),
                ('deleted', models.BooleanField(default=False, editable=False, verbose_name='Удалено?')),
                ('rev', models.CharField(default='1-e3ecb7b65c3d4068b286a5f2cb4c8afc', editable=False, max_length=64, verbose_name='Ревизия')),
                ('title', models.CharField(max_length=255, verbose_name='Наименование')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='subcategories', to='catalog.Category', verbose_name='Класс')),
                ('created_by', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Кем создано')),
                ('updated_by', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Кем обновлено')),
            ],
            options={
                'verbose_name': 'Вид (подкласс)',
                'verbose_name_plural': 'Виды (подклассы)',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='subcategory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='products', to='catalog.Subcategory', verbose_name='Вид'),
        ),
        migrations.AddField(
            model_name='product',
            name='updated_by',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Кем обновлено'),
        ),
        migrations.AddField(
            model_name='listing',
            name='manufacturer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='listings', to='catalog.Manufacturer', verbose_name='Производитель'),
        ),
        migrations.AddField(
            model_name='listing',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='listings', to='catalog.Product', verbose_name='Товар'),
        ),
        migrations.AddField(
            model_name='listing',
            name='updated_by',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Кем обновлено'),
        ),
        migrations.AddField(
            model_name='attribute',
            name='subcategory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='attributes', to='catalog.Subcategory', verbose_name='Вид (подкласс)'),
        ),
        migrations.AddField(
            model_name='attribute',
            name='updated_by',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Кем обновлено'),
        ),
    ]
