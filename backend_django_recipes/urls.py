"""backend_django_recipes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from backend_django_recipes.views import list_view, author_detail, recipe_detail

from backend_django_recipes.models import Author
admin.site.register(Author)

from backend_django_recipes.models import Recipes
admin.site.register(Recipes)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", list_view),
    path("author/<str:name>", author_detail),
    path("<str:name>/recipes/<str:title>", author_detail, recipe_detail)
]
