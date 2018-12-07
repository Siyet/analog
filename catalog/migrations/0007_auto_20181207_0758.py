# Generated by Django 2.1.3 on 2018-12-07 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_auto_20181207_0755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attribute',
            name='id',
            field=models.UUIDField(default='034c474b0da64e979928923aacc0d339', editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='attribute',
            name='rev',
            field=models.CharField(default='1-28174a7fae8d442cb226a9eac787c511', editable=False, max_length=64, verbose_name='Ревизия'),
        ),
        migrations.AlterField(
            model_name='attributevalue',
            name='id',
            field=models.UUIDField(default='034c474b0da64e979928923aacc0d339', editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='attributevalue',
            name='rev',
            field=models.CharField(default='1-28174a7fae8d442cb226a9eac787c511', editable=False, max_length=64, verbose_name='Ревизия'),
        ),
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.UUIDField(default='034c474b0da64e979928923aacc0d339', editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='category',
            name='rev',
            field=models.CharField(default='1-28174a7fae8d442cb226a9eac787c511', editable=False, max_length=64, verbose_name='Ревизия'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='id',
            field=models.UUIDField(default='034c474b0da64e979928923aacc0d339', editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='listing',
            name='rev',
            field=models.CharField(default='1-28174a7fae8d442cb226a9eac787c511', editable=False, max_length=64, verbose_name='Ревизия'),
        ),
        migrations.AlterField(
            model_name='manufacturer',
            name='id',
            field=models.UUIDField(default='034c474b0da64e979928923aacc0d339', editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='manufacturer',
            name='rev',
            field=models.CharField(default='1-28174a7fae8d442cb226a9eac787c511', editable=False, max_length=64, verbose_name='Ревизия'),
        ),
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.UUIDField(default='034c474b0da64e979928923aacc0d339', editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='rev',
            field=models.CharField(default='1-28174a7fae8d442cb226a9eac787c511', editable=False, max_length=64, verbose_name='Ревизия'),
        ),
        migrations.AlterField(
            model_name='specification',
            name='id',
            field=models.UUIDField(default='034c474b0da64e979928923aacc0d339', editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='specification',
            name='rev',
            field=models.CharField(default='1-28174a7fae8d442cb226a9eac787c511', editable=False, max_length=64, verbose_name='Ревизия'),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='id',
            field=models.UUIDField(default='034c474b0da64e979928923aacc0d339', editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='rev',
            field=models.CharField(default='1-28174a7fae8d442cb226a9eac787c511', editable=False, max_length=64, verbose_name='Ревизия'),
        ),
    ]
