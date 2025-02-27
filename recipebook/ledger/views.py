from django.views.generic import ListView, DetailView
from .models import Recipe

# Create your views here.

class RecipeListView(ListView):
    model = Recipe
    template_name = 'recipes/recipelist.html'
    context_object_name = 'recipes'

class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'recipes/recipe_detail.html'
    context_object_name = 'recipe'
