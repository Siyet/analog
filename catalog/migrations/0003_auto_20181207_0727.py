# Generated by Django 2.1.3 on 2018-12-07 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20181206_0317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attribute',
            name='id',
            field=models.UUIDField(default='b9ea3e5a25384997a2b608a61529f7b8', editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='attribute',
            name='rev',
            field=models.CharField(default='1-be7bb7e1fcd64b0a8433fbc5d96b73a5', editable=False, max_length=64, verbose_name='Ревизия'),
        ),
        migrations.AlterField(
            model_name='attributevalue',
            name='id',
            field=models.UUIDField(default='b9ea3e5a25384997a2b608a61529f7b8', editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='attributevalue',
            name='rev',
            field=models.CharField(default='1-be7bb7e1fcd64b0a8433fbc5d96b73a5', editable=False, max_length=64, verbose_name='Ревизия'),
        ),
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.UUIDField(default='b9ea3e5a25384997a2b608a61529f7b8', editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='category',
            name='rev',
            field=models.CharField(default='1-be7bb7e1fcd64b0a8433fbc5d96b73a5', editable=False, max_length=64, verbose_name='Ревизия'),
        ),
        migrations.AlterField(
            model_name='category',
            name='synonyms',
            field=models.CharField(blank=True, help_text='Вписывайте синонимы через точку с запятой', max_length=255, verbose_name='Синонимы'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='id',
            field=models.UUIDField(default='b9ea3e5a25384997a2b608a61529f7b8', editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='listing',
            name='rev',
            field=models.CharField(default='1-be7bb7e1fcd64b0a8433fbc5d96b73a5', editable=False, max_length=64, verbose_name='Ревизия'),
        ),
        migrations.AlterField(
            model_name='manufacturer',
            name='id',
            field=models.UUIDField(default='b9ea3e5a25384997a2b608a61529f7b8', editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='manufacturer',
            name='rev',
            field=models.CharField(default='1-be7bb7e1fcd64b0a8433fbc5d96b73a5', editable=False, max_length=64, verbose_name='Ревизия'),
        ),
        migrations.AlterField(
            model_name='manufacturer',
            name='synonyms',
            field=models.CharField(blank=True, help_text='Вписывайте синонимы через точку с запятой', max_length=255, verbose_name='Синонимы'),
        ),
        migrations.AlterField(
            model_name='product',
            name='attrs_values',
            field=models.ManyToManyField(to='catalog.AttributeValue', verbose_name='Атрибуты'),
        ),
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.UUIDField(default='b9ea3e5a25384997a2b608a61529f7b8', editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='rev',
            field=models.CharField(default='1-be7bb7e1fcd64b0a8433fbc5d96b73a5', editable=False, max_length=64, verbose_name='Ревизия'),
        ),
        migrations.AlterField(
            model_name='specification',
            name='id',
            field=models.UUIDField(default='b9ea3e5a25384997a2b608a61529f7b8', editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='specification',
            name='rev',
            field=models.CharField(default='1-be7bb7e1fcd64b0a8433fbc5d96b73a5', editable=False, max_length=64, verbose_name='Ревизия'),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='id',
            field=models.UUIDField(default='b9ea3e5a25384997a2b608a61529f7b8', editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='rev',
            field=models.CharField(default='1-be7bb7e1fcd64b0a8433fbc5d96b73a5', editable=False, max_length=64, verbose_name='Ревизия'),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='synonyms',
            field=models.CharField(blank=True, help_text='Вписывайте синонимы через точку с запятой', max_length=255, verbose_name='Синонимы'),
        ),
    ]
