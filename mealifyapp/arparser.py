import sys
import requests
from bs4 import BeautifulSoup
from mealifyapp.models import Recipe, Ingredient, Direction, Recipe_Ingredient

class ARParser:
    def __init__(self, url):
        self.url = url
        self.page = 1
        self.processCategory()

    def processCategory(self):
        try:
            r = requests.get(self.url+"&Page="+str(self.page))
            data = r.text
            soup = BeautifulSoup(data)
            for recipe in soup.find_all(id="divGridItemWrapper"):
                a = recipe.find('a')
                self.processRecipe("http://allrecipes.com"+a.get('href'))
            # self.page += 1
            # self.process()
        except Exception as e:
            print e

    def processRecipe(self, url):
        try:
            r = requests.get(url)
            data = r.text
            soup = BeautifulSoup(data)
            title = soup.find(id="itemTitle")
            calories = soup.find_all(id="lblNutrientValue")[0]
            r = Recipe(title=title.text, url=url, calories=calories.text)
            r.save()
            for ingredient in soup.find_all(id="liIngredient"):
                if ingredient.find(id="cbxIngredient"):
                    amt = ingredient.find(id="lblIngAmount")
                    name = ingredient.find(id="lblIngName")
                    if Ingredient.objects.filter(title=name.text).count() > 0:
                        i = Ingredient.objects.get(title=name.text)
                    else:
                        i = Ingredient(title=name.text)
                        i.save()
                    if amt is not None:
                        ri = Recipe_Ingredient(recipe=r,ingredient=i, amount=amt.text)
                        ri.save()
                        # print "\t" + amt.text + " " + name.text
                    elif not name.text.isspace():
                        ri = Recipe_Ingredient(recipe=r,ingredient=i, amount="")
                        ri.save()
                        # print "\t" + name.text
            directions = soup.find("div", class_="directLeft")
            for direction in directions.find_all("li"):
                d = Direction(recipe=r, text=direction.find("span").text)
                d.save()
        except Exception as e:
            print e
