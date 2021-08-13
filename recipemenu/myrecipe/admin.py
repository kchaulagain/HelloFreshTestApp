from django.contrib import admin
from myrecipe.models import WeeklyMenu,Recipe,Ingredients,Review
# Register your models here.
admin.site.register(WeeklyMenu)
admin.site.register(Recipe)
admin.site.register(Ingredients)
admin.site.register(Review)
