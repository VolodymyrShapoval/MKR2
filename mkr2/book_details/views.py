from django.shortcuts import render

# Create your views here.
def recipe_detail(request):
    return render(request, "recipe_detail.html")