from django.shortcuts import render, get_object_or_404
from .models import Book, Author

# Create your views here.
def main(request):
    books = Book.objects.all()
    authors = Author.objects.all()

    return render(request, "main.html", {'books': books, 'authors': authors})

def author_list(request):
    authors = Author.objects.all()
    return render(request, 'author_list.html', context={ 
        'authors': authors
    })
def author_detail(request, author_id):
    author= get_object_or_404(Author, id=author_id)
    return render(request, 'author_detail.html', context={ 
        'author': author
    })
def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', context={ 
        'books': books
    })
def book_detail(request, book_id):
    book= get_object_or_404(Book, id=book_id)
    return render(request, 'book_detail.html', context={ 
        'book': book
    })