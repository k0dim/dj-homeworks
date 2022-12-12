from django.shortcuts import render, redirect, get_object_or_404
from phones.models import Phone

def index(request):
    return redirect('catalog')

def get_data(parametr):
    list_all  = []
    for phone in Phone.objects.all().order_by(parametr):
        dict_one = {
            'id':phone.id,
            'name':phone.name,
            'price':phone.price,
            'image':phone.image,
            'slug':phone.slug,
            'release_date':phone.release_date,
            'lte_exists':phone.lte_exists,
        }
        list_all.append(dict_one) 
    return list_all

def show_catalog(request):
    list_all  = []
    if request.GET.get("sort") == 'name':
        list_all = get_data('name')
    elif request.GET.get("sort") == 'min_price':
        list_all = get_data('-price')
    elif request.GET.get("sort") == 'max_price':
        list_all = get_data('price')

    template = 'catalog.html'
    context = {
        'phones':list_all,
    }
    return render(request, template, context)


def show_product(request, slug):
    for phone in Phone.objects.all().filter(slug=slug):
        dict_one = {
            'id':phone.id,
            'name':phone.name,
            'image':phone.image,
            'slug':phone.slug,
            'release_date':phone.release_date,
            'lte_exists':phone.lte_exists,
            'price':phone.price,
        }
    template = 'product.html'
    context = {
        'phone':dict_one,
    }
    return render(request, template, context)
