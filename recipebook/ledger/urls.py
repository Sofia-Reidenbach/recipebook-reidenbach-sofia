from django.urls import path
from .views import RecipeListView, RecipeDetailView, RecipeCreateView, RecipeImageUploadView

urlpatterns = [
    path('',RecipeListView.as_view(),name='recipe_list'),
    path('recipes/list', RecipeListView.as_view(), name='recipe_list'),
    path('recipe/<int:pk>', RecipeDetailView.as_view(), name='recipe_detail'),
    path('recipe/<int:pk>/add_image/',
         RecipeImageUploadView.as_view(), name='recipe_image_upload'),
    path('recipe/add', RecipeCreateView.as_view(), name="recipe_add")
]

app_name = "ledger"
