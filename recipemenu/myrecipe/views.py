import json

from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist

from .serializers import WeeklyMenuSerializer
from .models import WeeklyMenu
from .serializers import RecipeSerializer
from .models import Recipe


def index(request):
    return HttpResponse("Hello, world.")

@api_view(["GET"])
@csrf_exempt
# @permission_classes([IsAuthenticated])  
def welcome(request):
    content = {"message": "Welcome to the BookStore!"}
    return JsonResponse(content)


# Get all Weekly Menus Rest Api
@api_view(["GET"])
# @csrf_exempt
@permission_classes([IsAuthenticated])
def get_menu(request):
    menu = WeeklyMenu.objects.all()
    serializer = WeeklyMenuSerializer(menu, many=True)
    return JsonResponse({'menus': serializer.data})


# Add Weekly Menu Rest Api
@api_view(["POST"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def add_menu(request):
    menu_name = request.POST['menu_name']
    user = request.user
    try:
        menu = WeeklyMenu.objects.create(
			menu_name = menu_name
        )
        serializer = WeeklyMenuSerializer(menu)
        return JsonResponse({'menus': serializer.data}, safe=False)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False)

#Update weekly menu Rest api
@api_view(["PUT"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def update_menu(request, menu_id):
    user = request.user.id
    menu_name = request.POST['menu_name']
    try:
        menu = WeeklyMenu.objects.filter(id=menu_id)
        menu.update( menu_name = menu_name)
        menu = WeeklyMenu.objects.get(id=menu_id)
        serializer = WeeklyMenuSerializer(menu)
        return JsonResponse({'menus': serializer.data}, safe=False)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False)
    except Exception as e:
        return JsonResponse({'error': str(e)}, safe=False)


#Delete weekly menu Resy api
@api_view(["DELETE"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def delete_menu(request, menu_id):
    user = request.user.id
    try:
        menu = WeeklyMenu.objects.filter(id=menu_id)
        menu.delete()
        return HttpResponse('deleted')
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False)
    except Exception as e:
        return JsonResponse({'error': str(e)}, safe=False)



#Get all recipes of some weekly menu
@api_view(["POST"])
@csrf_exempt
@permission_classes([IsAuthenticated])
# def get_recipe(request):
#     recipe = Recipe.objects.all()
#     serializer = RecipeSerializer(recipe, many=True)
#     return JsonResponse({'recipes': serializer.data})
def get_recipe(request):
    try:
        menu_id = request.POST.get('menu_id')
        recipe = Recipe.objects.filter(menu__id=menu_id)
        serializer = RecipeSerializer(recipe, many=True)
        return JsonResponse({'recipes': serializer.data,'recipe_menu_id':menu_id})
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False)
    except Exception as e:
        return JsonResponse({'error': str(e)}, safe=False)


#Add recipes of some weekly menu
@api_view(["POST"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def add_recipe(request):
    menus = WeeklyMenu.objects.filter(id=request.POST['menu_id'])
    recipe_name = request.POST['recipe_name']
    instructions = request.POST['instructions']
    classification = request.POST['classification']
    metadata = request.POST['metadata']
    user = request.user
    try:
        recipe = Recipe.objects.create(
            recipe_name = recipe_name,
            instructions = instructions,
            classification = classification,
            metadata = metadata,
        )
        recipe.menu.set(menus)
        serializer = RecipeSerializer(recipe)
        return JsonResponse({'recipes': serializer.data}, safe=False)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False)
    except Exception as e:
        return JsonResponse({'error': str(e)}, safe=False)


#delete recipe of some weekly menu
@api_view(["DELETE"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def delete_recipe(request, recipe_id):
    user = request.user.id
    try:
        recipe = Recipe.objects.filter(id=recipe_id)
        recipe.delete()
        return HttpResponse('deleted')
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False)
    except Exception as e:
        return JsonResponse({'error': str(e)}, safe=False)        



#update recipe of some weekly menu
@api_view(["PUT"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def update_recipe(request, recipe_id):
    user = request.user.id
    recipe_name = request.POST['recipe_name']
    instructions = request.POST['instructions']
    classification = request.POST['classification']
    metadata = request.POST['metadata']
    try:
        recipe = Recipe.objects.filter(id=recipe_id)
        recipe.update(recipe_name = recipe_name,
            instructions = instructions,
            classification = classification,
            metadata = metadata)
        recipe = Recipe.objects.get(id=recipe_id)
        serializer = RecipeSerializer(recipe)
        return JsonResponse({'recipes': serializer.data}, safe=False)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False)
    except Exception as e:
        return JsonResponse({'error': str(e)}, safe=False)
