# Generated by Django 5.1.4 on 2024-12-15 16:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_alter_product_options_product_a'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='a',
        ),
    ]
