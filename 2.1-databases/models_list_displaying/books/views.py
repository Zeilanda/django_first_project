from django.shortcuts import render

from books.models import Book


def books_view(request):
    template = 'books/books_list.html'
    context = {'books': Book.objects.all()}
    return render(request, template, context)


def book_detail(request, slug):
    template = 'books/book_detail.html'
    context = {'books': Book.objects.filter(pub_date=slug)}
    return render(request, template, context)

