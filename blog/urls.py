from django.urls import path
from . import views
from .views import HomeView, TheRecipeView, CreateRecipeView, EditRecipeView, DeleteRecipeView, CategoryList #CategoryView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('recipe/<int:pk>', TheRecipeView.as_view(), name="the_recipe"),
    path('create/', CreateRecipeView.as_view(), name="create_recipe"),
    path('recipe/edit/<int:pk>', EditRecipeView.as_view(), name="edit_recipe"),
    path('recipe/<int:pk>/delete', DeleteRecipeView.as_view(), name="delete_recipe"),
    #path('categories/', views.Category, name="categories"),
    path('category/<str:cat>/', CategoryList, name="category"),
]
