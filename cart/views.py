from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from data.models import Product
from .cart import Cart
from .forms import CartAddProductForm


@require_POST
def cart_add(request, product_id):
    print("text")
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    print(request)
    print(form)
    print(product)
    if form.is_valid():
        print("text1")
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
        print(cart)
    return redirect('cart:cart_detail')

def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')

def cart_detail(request):
    cart = Cart(request)

    return render(request, 'cart.html', {'cart': cart})

def contextbacket(request):

    return render(request, 'contextbacket.html')