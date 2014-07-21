from django.contrib import admin
from mealifyapp.models import Recipe, Ingredient, Recipe_Ingredient, Direction

class DirectionAdmin(admin.StackedInline):
    model = Direction
    extra = 0

class RecipeAdmin(admin.ModelAdmin):
    fields = ['title', 'url', 'calories']
    inlines = [DirectionAdmin]
    list_display = ['title', 'url', 'calories', 'created_at']
    search_fields = ['title']

class RecipeIngredientAdmin(admin.ModelAdmin):
    fields = ['recipe', 'ingredient', 'amount']

class IngredientAdmin(admin.ModelAdmin):
    search_fields = ['title']


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe_Ingredient, RecipeIngredientAdmin)
