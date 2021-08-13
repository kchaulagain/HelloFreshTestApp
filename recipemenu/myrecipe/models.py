from django.db import models

#WeeklyMenu Model
class WeeklyMenu(models.Model):
	menu_name = models.CharField(max_length = 50)

	def __str__(self):
		return self.menu_name

#Recipe Model 
class Recipe(models.Model):
	menu = models.ManyToManyField(WeeklyMenu, null = True, blank = True)
	recipe_name = models.CharField(max_length = 50, null = True, blank = True)
	instructions = models.TextField(null = True, blank = True)
	classification = models.CharField(max_length = 20, null = True, blank = True)
	metadata = models.TextField(null = True, blank = True)


	def __str__(self):
		return self.recipe_name

#Ingredients Model
class Ingredients(models.Model):
	recipe = models.ManyToManyField(Recipe)
	ingredient_name = models.CharField(max_length = 50, null = True, blank = True)
	nutritional_info = models.TextField(null = True, blank = True)

	def __str__(self):
		return self.ingredient_name

#Review Model
class Review(models.Model):
	recipe = models.ForeignKey(Recipe, on_delete = models.CASCADE ,null = True, blank = True )
	rating = models.IntegerField(null = True, blank = True)
	comments = models.TextField(null = True, blank = True)
		
