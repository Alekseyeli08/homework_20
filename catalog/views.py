from django.shortcuts import render

from catalog.models import Product


def home(request):
    product = Product.objects.all()
    context = {'product': product}
    return render(request, 'catalog/product_list.html', context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f"Имя пользователя : {name}\nТелефон: {phone}\nСообщение: {message}\n")

    return render(request, 'catalog/contacts.html')


def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    context = {'product': product}
    return render(request, 'catalog/product_detail.html', context)


def add_product(request):
    return render(request, 'catalog/product_add.html')


# def add_bd_prod(request):
#     if request.method == 'POST':
#         new_product = Product.object.create(name='name', description='description', image='image', )
#         return  new_product