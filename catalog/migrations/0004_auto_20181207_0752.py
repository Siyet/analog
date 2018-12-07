# Generated by Django 2.1.3 on 2018-12-07 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_auto_20181207_0727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attribute',
            name='id',
            field=models.UUIDField(default='05972732cc524b6ba8b716f69ca1401f', editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='attribute',
            name='rev',
            field=models.CharField(default='1-1c9b96a246c545feb1d1254e521b0af2', editable=False, max_length=64, verbose_name='Ревизия'),
        ),
        migrations.AlterField(
            model_name='attributevalue',
            name='id',
            field=models.UUIDField(default='05972732cc524b6ba8b716f69ca1401f', editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='attributevalue',
            name='rev',
            field=models.CharField(default='1-1c9b96a246c545feb1d1254e521b0af2', editable=False, max_length=64, verbose_name='Ревизия'),
        ),
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.UUIDField(default='05972732cc524b6ba8b716f69ca1401f', editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='category',
            name='rev',
            field=models.CharField(default='1-1c9b96a246c545feb1d1254e521b0af2', editable=False, max_length=64, verbose_name='Ревизия'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='id',
            field=models.UUIDField(default='05972732cc524b6ba8b716f69ca1401f', editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='listing',
            name='rev',
            field=models.CharField(default='1-1c9b96a246c545feb1d1254e521b0af2', editable=False, max_length=64, verbose_name='Ревизия'),
        ),
        migrations.AlterField(
            model_name='manufacturer',
            name='id',
            field=models.UUIDField(default='05972732cc524b6ba8b716f69ca1401f', editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='manufacturer',
            name='rev',
            field=models.CharField(default='1-1c9b96a246c545feb1d1254e521b0af2', editable=False, max_length=64, verbose_name='Ревизия'),
        ),
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.UUIDField(default='05972732cc524b6ba8b716f69ca1401f', editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='rev',
            field=models.CharField(default='1-1c9b96a246c545feb1d1254e521b0af2', editable=False, max_length=64, verbose_name='Ревизия'),
        ),
        migrations.AlterField(
            model_name='specification',
            name='id',
            field=models.UUIDField(default='05972732cc524b6ba8b716f69ca1401f', editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='specification',
            name='rev',
            field=models.CharField(default='1-1c9b96a246c545feb1d1254e521b0af2', editable=False, max_length=64, verbose_name='Ревизия'),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='id',
            field=models.UUIDField(default='05972732cc524b6ba8b716f69ca1401f', editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='rev',
            field=models.CharField(default='1-1c9b96a246c545feb1d1254e521b0af2', editable=False, max_length=64, verbose_name='Ревизия'),
        ),
    ]