from django.shortcuts import render
from django.views import View
from .models import Produto


class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'home/index.html')

# class Produtos(View):
#     def get(self, request, *args, **kwargs):

#        produtos = Produto.objects.filter()

#         context = {
#             'produtos': produtos,
#         }

#         return render(request, 'home/catalogo.html', context)


class Roupas(View):
    def get (self, request, *args, **kargs):
        roupas = Produto.objects.filter(categoria__name__contains='roupas')
        
        context  = {
            'roupas': roupas,
        }

        return render(request, 'home/roupas.html', context)


class Perfumes(View):
     def get (self, request, *args, **kargs):
        perfumes = Produto.objects.filter(categoria__name__contains='perfumes')
        
        context  = {
            'perfumes': perfumes,
        }

        return render(request, 'home/perfumes.html', context)


class Cosmeticos(View):
     def get (self, request, *args, **kargs):
        cosmeticos = Produto.objects.filter(categoria__name__contains='cosmeticos')
        
        context  = {
            'cosmeticos': cosmeticos,
        }

        return render(request, 'home/cosmeticos.html', context)

     
