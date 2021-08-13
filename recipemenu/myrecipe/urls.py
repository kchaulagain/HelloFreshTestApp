from . import views

from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('', TemplateView.as_view(template_name = 'index.html'),name = 'home'),
    path('api/',views.welcome),
    path('api/get_menu/',views.get_menu, name='get all menus'),
    path('api/add_menu/',views.add_menu, name='add menu'),
    path('api/update_menu/<int:menu_id>/',views.update_menu, name='update menu'),
    path('api/delete_menu/<int:menu_id>/',views.delete_menu, name='update menu'),                         
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/get_recipe/',views.get_recipe, name='get_all_recipe'), 
    path('api/add_recipe/',views.add_recipe, name='add_recipe'),
    path('api/update_recipe/<int:recipe_id>/',views.update_recipe, name='update recipe'),
    path('api/delete_recipe/<int:recipe_id>/',views.delete_recipe, name='delete recipe'),              
]
