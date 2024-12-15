from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def get_product_view(request, product_id):
    # if product with product_id exists assign it to product else return a bad request
    try:
        product = Product.objects.get(id=product_id)
    except ObjectDoesNotExist:
        return HttpResponse("Bad request", status=400)

    if request.method == "GET":
        # We just return a string with all the data about the product.
        return HttpResponse(f"{product.name} {product.quantity} {product.quality}", status=200)
    else:
        return HttpResponse("Bad request", status=400)

@login_required
def delete_product_view(request, product_id):
    pass

@login_required
def create_product_view(request):
    pass