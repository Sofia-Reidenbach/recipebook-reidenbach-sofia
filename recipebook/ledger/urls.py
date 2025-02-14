from django.urls import path

from .views import RecipeList, Recipe1, Recipe2

#from django.contrib import admin
#from django.urls import include, path

urlpatterns = [
    path('recipes/list', RecipeList, name='Recipe List'),
    path('recipe/1', Recipe1, name='Recipe 1'),
    path('recipe/2', Recipe2, name='Recipe 2')
]
# This might be needed, depending on your Django version
app_name = "ledger"