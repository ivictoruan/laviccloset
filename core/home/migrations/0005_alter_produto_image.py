# Generated by Django 3.2.7 on 2021-10-25 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_produto_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='image',
            field=models.ImageField(upload_to='products_images/'),
        ),
    ]
