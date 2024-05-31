from django.shortcuts import render
from .models import Book

# Create your views here.
def main(request):
    books = Book.objects.all()

    return render(request, "main.html", {'books': books})
