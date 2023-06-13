from django.shortcuts import render
from .models import(
     Product, Category,
     Color, Size, Country, Brand
)
from django.shortcuts import get_list_or_404

from datetime import datetime


'''--------------------------------------------------'''


def index(request):
     trend = get_list_or_404(
          Product,
          trend=True
     )

     year = datetime.now().strftime('%Y')
     month = datetime.now().strftime('%m')

     new = Product.objects.filter(
          date__year=year,
          date__month=month
     )

     return render(
          request, 'index.html',
          {
               'trend': trend,
               'new': new
          }
     )

def by_category(request, slug):
    products = Product.objects.filter(category=slug)
    categories = Category.objects.all()
    current_category = Category.objects.get(slug=category_id)
    context = {
        'products': products,
        'categories': categories,
        'current_category': current_category,
    }
    return render(request, 'onshop/categories.html', context)


def product_list(request):
     return render(
          request, 'shop/product_list.html',
          {
               'products': Product.objects.all()
          }
     )

def product_detail(request, pk):
     return render(
          request, 'shop/product_detail.html',
          {
               'product': Product.objects.get(id=pk)
          }
     )


'''--------------------------------------------------'''


def contacts(request):
     return render(
          request, 'contact.html'
     )

def liked(request):
     return render(
          request, 'liked.html'
     )