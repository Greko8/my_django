from django.shortcuts import render, redirect
from phones.models import Phone

def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get('sort', 'id')
    reverse = False
    if sort == 'min_price':
        sort = 'price'
    if sort == 'max_price':
        reverse = True
        sort = 'price'

    phone_objects = Phone.objects.all()
    phones_list = []
    for p in phone_objects:
        phs = {
            'id': p.id,
            'name': p.name,
            'price': p.price,
            'image': p.image,
            'release_date': p.release_date,
            'slug': p.slug
        }
        phones_list.append(phs)
    if sort:
        phones_list = sorted(phones_list, key=lambda x: x[sort], reverse=reverse)
    context = {
        'phones': phones_list
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone1 = Phone.objects.get(slug=slug)
    phone = {
        'id': phone1.id,
        'name': phone1.name,
        'price': phone1.price,
        'image': phone1.image,
        'release_date': phone1.release_date,
        'slug': phone1.slug
    }
    context = {
        'phone': phone
    }
    return render(request, template, context)
