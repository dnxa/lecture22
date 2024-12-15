from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from .forms import ProductModelForm


# Create your views here.
@login_required
def get_product_view(request, product_id):
    # if product with product_id exists assign it to product else return a bad request
    try:
        product = Product.objects.get(id=product_id)
    except ObjectDoesNotExist:
        return HttpResponse("Bad request", status=400)

    if request.method == "GET" and product.user == request.user:
        # We just return a string with all the data about the product.
        return HttpResponse(f"{product.name} {product.quantity} {product.quality}", status=200)
    else:
        return HttpResponse("Bad request", status=400)

''' 
Don't know how to test this with the user and the delete command
because i cant sent delete request from a template and with test I cant be logged in so...
It should work though.
'''
@login_required
def delete_product_view(request, product_id):
    if request.method == "GET":
        product = Product.objects.get(id=product_id)

        # Only delete if we are its creator.
        if product.user == request.user:
            product.delete()
            return HttpResponse("Product deleted", status=400)

        return HttpResponse("Bad request", status=400)
    else:
        return HttpResponse("Bad request", status=400)

@login_required
def create_product_view(request):
    if request.method == "GET":
        form = ProductModelForm()

        # Render the creation field.
        return render(request, "productcreate.html", {'form':form})
    elif request.method == "POST":
        form = ProductModelForm(request.POST)
        if form.is_valid():
            # Apparently form.save() returns the model so we can get the id and redirect to get_product_view with it.
            model = form.save()

            # Make the creator the user of the model they created.
            model.user = request.user

            # We have to save it after we modify it.
            model.save()

            # Redirect to the model we created.
            return redirect(f"/product/{model.id}/", status=200)

        return HttpResponse("Bad request", status=400)
    else:
        return HttpResponse("Bad request", status=400)