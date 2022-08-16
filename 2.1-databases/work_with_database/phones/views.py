from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get('sort')
    if sort == 'name':
        context = {'phones': Phone.objects.order_by('name').all()}
        return render(request, template, context)
    elif sort == 'min_price':
        context = {'phones': Phone.objects.order_by('price').all()}
        return render(request, template, context)
    elif sort == 'max_price':
        context = {'phones': Phone.objects.order_by('-price').all()}
        return render(request, template, context)
    context = {'phones': Phone.objects.all()}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {'phone': Phone.objects.get(slug=slug)}
    return render(request, template, context)
