# Generated by Django 3.2.7 on 2021-10-22 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=400)),
                ('image', models.ImageField(upload_to='img/products_images/')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('is_vendido', models.BooleanField(default=False)),
            ],
        ),
        migrations.RenameModel(
            old_name='Category',
            new_name='Categoria',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.AddField(
            model_name='produto',
            name='categoria',
            field=models.ManyToManyField(related_name='item', to='home.Categoria'),
        ),
    ]