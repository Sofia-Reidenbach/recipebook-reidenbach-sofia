from django import forms
from .models import Recipe, RecipeImage


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'
        widgets = {
            'created_on': forms.TextInput(attrs={'type': 'datetime-local'}),
            'updated_on': forms.TextInput(attrs={'type': 'datetime-local'}),
        }


class RecipeImageForm(forms.ModelForm):
    class Meta:
        model = RecipeImage
        fields = ["image", "description",]
