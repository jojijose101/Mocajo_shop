from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator,InvalidPage,EmptyPage
from .models import Category, Product


# Create your views here.

# def index(request):
#     return HttpResponse('hello my app')


def allproductcat(request,c_slug=None):
    c_page = None
    products_list = None

    if c_slug !=None:
        c_page = get_object_or_404(Category,slug=c_slug)
        products_list = Product.objects.all().filter(category=c_page,available=True)
    else:
        products_list = Product.objects.all().filter(available=True)
    pagenator = Paginator(products_list,6)
    try:
        page= int(request.GET.get('page','1'))
    except:
        page=1
    try:
        products = pagenator.page(page)
    except(InvalidPage,EmptyPage):
        products = pagenator.page(pagenator.num_pages)



    return render(request,'category.html',{'category':c_page,'products':products})


def product(request,c_slug,p_slug):
    try:
        products = Product.objects.get(category__slug=c_slug,slug=p_slug)
    except Exception as e:
        print("error")
        raise e
    return render(request,'product.html',{'products':products})