from django.db import models

class Produto(models.Model):
    categoria = models.ManyToManyField('Categoria', related_name='produto') # o que esse related name faz?
    name = models.CharField(max_length=200, verbose_name="Nome")
    description = models.TextField(max_length=400, verbose_name="Descrição")
    image = models.ImageField(upload_to='products_images/', verbose_name="Imagem") 
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Preço")
    created_on = models.DateTimeField(auto_now_add=True, verbose_name="Criado em")
    is_vendido = models.BooleanField(default=False, verbose_name="Vendido", help_text="O produto foi vendido?")
    # fazer um campo para saber o valor que foi comprado == initial_price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Preço Inicial")
    is_avaliable = models.BooleanField(default=True, verbose_name="Disponível", help_text="Está disponível?")

    objects = models.Manager()
  
    class Meta:
        ordering = ("name",)

    def __str__(self):
        return f'{self.name} - R${self.price}'
        # return self.name


class Categoria(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name