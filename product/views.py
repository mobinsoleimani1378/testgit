from django.shortcuts import render
from .models import Product


def product(request, id):
    product = Product.objects.get(id=id)
    a = product.attributs.all()
    b=[]
    d=[]
    s=0
    for i in a:
        s+=1
        for j in i.attributsdetaill.all():
            if s==1:
                b.append(j)
            else:
                d.append(j)
    print(s)
    return render(request, 'product/product.html', {'product': product, 'b':b, 'd':d})
