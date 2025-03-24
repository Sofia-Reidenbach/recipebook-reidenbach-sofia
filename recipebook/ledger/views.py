from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Recipe, RecipeImage
from .forms import RecipeForm
from .forms import RecipeImageForm
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class RecipeListView(ListView):
    model = Recipe
    template_name = 'recipes/recipelist.html'
    context_object_name = 'recipes'
    

class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'recipes/recipe_detail.html'
    context_object_name = 'recipe'


class RecipeCreateView(CreateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'recipes/recipe_add.html'


class RecipeUpdateView(UpdateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'recipe_detail.html'


class RecipeImageUploadView(LoginRequiredMixin, CreateView):
    model = RecipeImage
    form_class = RecipeImageForm
    template_name = "recipes/recipe_image_upload.html"

    def form_valid(self, form):
        form.instance.recipe_id = self.kwargs["pk"]
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["recipe"] = Recipe.objects.get(pk=self.kwargs["pk"])
        return ctx

    def get_success_url(self):
        return reverse("ledger:recipe_detail", kwargs={"pk": self.kwargs["pk"]})
