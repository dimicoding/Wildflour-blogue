from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Recipe
from .forms import RecipeForm, EditForm
from django.urls import reverse_lazy

class HomeView(ListView):
    model = Recipe
    template_name = "list-view.html"
    

class TheRecipeView(DetailView):
    model = Recipe
    template_name = "the-recipe.html"


class CreateRecipeView(CreateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'create.html'


class EditRecipeView(UpdateView):
    model = Recipe
    form_class = EditForm
    template_name = 'edit-recipe.html'


class DeleteRecipeView(DeleteView):
    model = Recipe
    template_name = 'delete-recipe.html'
    success_url = reverse_lazy('home')
    
