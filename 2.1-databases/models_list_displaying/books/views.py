from django.shortcuts import render
from json import load
from django.core.paginator import Paginator
from books.models import Book

def books_view(request):
    with open('fixtures/books.json', 'r') as jsonfile:
        for example in load(jsonfile):
            if len([q for q in Book.objects.filter(id=example['pk'])]) == 0:
                new_book = Book(
                    id=example['pk'],
                    name=example['fields']['name'],
                    author=example['fields']['author'],
                    pub_date=example['fields']['pub_date']
                )
                new_book.save()

    list_all  = []
    for books in Book.objects.all():
        dict_one = {
            'name':books.name,
            'author':books.author,
            'pub_date':f'{books.pub_date}',
        }
        list_all.append(dict_one)

    template = 'books/books_list.html'
    context = {
        'list_all': list_all,
    }
    return render(request, template, context)

def pagination_book(request, pub_date):

    pub_dates = [f'{q.pub_date}' for q in Book.objects.all().order_by('pub_date').distinct()]
    # ['2012-05-16', '2016-12-06', '2018-02-27', '2020-01-29']

    paginator = Paginator(pub_dates, 1)
    page = paginator.page(paginator.object_list.index(pub_date) + 1)
    if page.has_next():
        pub_date_next = pub_dates[page.number]
    if page.has_previous():
        pub_date_previous = pub_dates[page.number-2]

    list_all  = []
    for books in Book.objects.filter(pub_date=pub_date):
        dict_one = {
            'name':books.name,
            'author':books.author,
            'pub_date':f'{books.pub_date}',
        }
        list_all.append(dict_one)

    template = 'books/books_list.html'
    context = {
        'list_all':list_all,
        'page':page,
        'pub_date_next':pub_date_next,
        'pub_date_previous':pub_date_previous,
        'pub_date':pub_date,
    }
    return render(request, template, context)



