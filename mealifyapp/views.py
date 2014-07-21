from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse
from mealifyapp.models import Recipe

def index(request):
    return render_to_response('mealifyapp/index.html')

def recipes(request):
    recipes = Recipe.objects.all()
    return render_to_response('mealifyapp/recipes.html', {'recipes':recipes})

def recipe(request, recipe_id):
    r = get_object_or_404(Recipe, pk=recipe_id)
    return render_to_response('mealifyapp/recipe.html', {'recipe':r})
