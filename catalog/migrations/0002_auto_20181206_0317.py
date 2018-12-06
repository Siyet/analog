# Generated by Django 2.1.3 on 2018-12-06 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.AddField(
            model_name='category',
            name='synonyms',
            field=models.CharField(default='', help_text='Вписывайте синонимы через точку с запятой', max_length=255, verbose_name='Синонимы'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='manufacturer',
            name='synonyms',
            field=models.CharField(default='', help_text='Вписывайте синонимы через точку с запятой', max_length=255, verbose_name='Синонимы'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='attrs_values',
            field=models.ManyToManyField(to='catalog.AttributeValue'),
        ),
        migrations.AddField(
            model_name='product',
            name='title',
            field=models.CharField(default='', max_length=255, verbose_name='Наименование'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='specification',
            name='listings',
            field=models.ManyToManyField(to='catalog.Listing'),
        ),
        migrations.AddField(
            model_name='subcategory',
            name='synonyms',
            field=models.CharField(default='', help_text='Вписывайте синонимы через точку с запятой', max_length=255, verbose_name='Синонимы'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='attribute',
            name='id',
            field=models.UUIDField(default='1adb3270894e40cbaa13aaf87f7c6735', editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='attribute',
            name='rev',
            field=models.CharField(default='1-82008c682c0441c3baaf907e47327b52', editable=False, max_length=64, verbose_name='Ревизия'),
        ),
        migrations.AlterField(
            model_name='attributevalue',
            name='id',
            field=models.UUIDField(default='1adb3270894e40cbaa13aaf87f7c6735', editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='attributevalue',
            name='rev',
            field=models.CharField(default='1-82008c682c0441c3baaf907e47327b52', editable=False, max_length=64, verbose_name='Ревизия'),
        ),
        migrations.AlterField(
            model_name='attributevalue',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Значение'),
        ),
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.UUIDField(default='1adb3270894e40cbaa13aaf87f7c6735', editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='category',
            name='rev',
            field=models.CharField(default='1-82008c682c0441c3baaf907e47327b52', editable=False, max_length=64, verbose_name='Ревизия'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='id',
            field=models.UUIDField(default='1adb3270894e40cbaa13aaf87f7c6735', editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='listing',
            name='rev',
            field=models.CharField(default='1-82008c682c0441c3baaf907e47327b52', editable=False, max_length=64, verbose_name='Ревизия'),
        ),
        migrations.AlterField(
            model_name='manufacturer',
            name='id',
            field=models.UUIDField(default='1adb3270894e40cbaa13aaf87f7c6735', editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='manufacturer',
            name='rev',
            field=models.CharField(default='1-82008c682c0441c3baaf907e47327b52', editable=False, max_length=64, verbose_name='Ревизия'),
        ),
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.UUIDField(default='1adb3270894e40cbaa13aaf87f7c6735', editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='rev',
            field=models.CharField(default='1-82008c682c0441c3baaf907e47327b52', editable=False, max_length=64, verbose_name='Ревизия'),
        ),
        migrations.AlterField(
            model_name='specification',
            name='id',
            field=models.UUIDField(default='1adb3270894e40cbaa13aaf87f7c6735', editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='specification',
            name='rev',
            field=models.CharField(default='1-82008c682c0441c3baaf907e47327b52', editable=False, max_length=64, verbose_name='Ревизия'),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='id',
            field=models.UUIDField(default='1adb3270894e40cbaa13aaf87f7c6735', editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='rev',
            field=models.CharField(default='1-82008c682c0441c3baaf907e47327b52', editable=False, max_length=64, verbose_name='Ревизия'),
        ),
    ]