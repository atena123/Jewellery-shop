from django.shortcuts import render
from products.models import Product

# Create your views here.
def do_search(request):
    products = Product.objects.filter(name__icontains=request.GET['search'])
    return render(request, "products.html", {"products": products})
