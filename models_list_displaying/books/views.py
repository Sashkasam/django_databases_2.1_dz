from django.shortcuts import render
from django.core.paginator import Paginator
from books.models import Book


def books_view(request):
    template = 'books/books_list.html'
    all_book = Book.objects.all()
    context = {'books': all_book,



    }
    return render(request, template, context)




def show_pub_date_view(request, date):
    template = 'books/book.html'
    try:
        prev_date = Book.objects.filter(pub_date__lt=date).values('pub_date').first()['pub_date'].strftime('%Y-%m-%d')
    except TypeError:
        prev_date = ''
    try:
        next_date = Book.objects.filter(pub_date__gt=date).values('pub_date').first()['pub_date'].strftime('%Y-%m-%d')
    except TypeError:
        next_date = ''
    context = {
        'books': Book.objects.filter(pub_date__iexact=date),
        'prev': prev_date,
        'next': next_date,
    }
    print(context)
    return render(request, template, context)