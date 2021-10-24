from django.db import models

class Produto(models.Model):
    categoria = models.ManyToManyField('Categoria', related_name='produto') # o que esse related name faz?
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=400)
    image = models.ImageField(upload_to='img/products_images/') 
    price = models.DecimalField(max_digits=5, decimal_places=2)
    created_on = models.DateTimeField(auto_now_add=True)
    is_vendido = models.BooleanField(default=False)
    # fazer um campo para saber o valor que foi comprado
    is_available = models.BooleanField(default=True)

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