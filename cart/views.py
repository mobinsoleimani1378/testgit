from django.shortcuts import render, redirect, get_object_or_404
from product.models import Product
from .cart_module import Cart


def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/cart.html', {'cart': cart})


def cart_add(request, pk):
    if request.method == 'POST':
        product = get_object_or_404(Product, id=pk)
        size, color, quantity = request.POST.get('size', 'empty'), request.POST.get('color', 'empty'), request.POST.get(
            'quantity')
        cart = Cart(request)
        cart.add(product, quantity, color, size)
        return redirect('cart:cart_detail')


def cart_delete(request, id):
    cart = Cart(request)
    cart.delete(id)
    return redirect('cart:cart_detail')