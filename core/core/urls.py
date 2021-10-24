"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from home.views import Index, Roupas, Perfumes, Cosmeticos # obrigatoriamente mudei o nome da var, por conta de um erro que estava sendo gerado por alguma coincidencia de nomes de vars.
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Index.as_view(), name='index'),
    path('roupas/', Roupas.as_view(), name='roupas'), # atenção nos nomes.
    path('perfumes/', Perfumes.as_view(), name='perfumes'),
    path('cosmeticos/', Cosmeticos.as_view(), name='cosmeticos'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

