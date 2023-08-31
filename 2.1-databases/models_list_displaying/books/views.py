from django.core.paginator import Paginator
from django.shortcuts import render
from books.models import Book


def books_view(request, pub_date=None):
    template = 'books/books_list.html'
    if pub_date:
        books_object = Book.objects.filter(pub_date=pub_date)
    else:
        books_object = Book.objects.all()
    books = []
    for b in books_object:
        book = {
            'name': b.name,
            'author': b.author,
            'pub_date': str(b.pub_date),
        }
        books.append(book)
    books = sorted(books, key=lambda x: x['pub_date'])

    context = {
        'books': books
    }
    return render(request, template, context)
