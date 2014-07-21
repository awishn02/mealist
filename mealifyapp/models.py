from django.db import models

class Recipe(models.Model):
    title = models.CharField(max_length=50)
    url = models.CharField(max_length=255, unique=True)
    calories = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title

class Direction(models.Model):
    recipe = models.ForeignKey(Recipe)
    text = models.TextField()

    def __unicode__(self):
        return self.text

class Ingredient(models.Model):
    title = models.CharField(max_length=50, unique=True)
    recipes = models.ManyToManyField(Recipe, through='Recipe_Ingredient')

    def __unicode__(self):
        return self.title

class Recipe_Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe)
    ingredient = models.ForeignKey(Ingredient)
    amount = models.CharField(max_length=50)

    def __unicode__(self):
        return self.amount + " of " + self.ingredient.title + " in: " + self.recipe.title
