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
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        category = request.POST.get('category')
        created_at = request.POST.get('created_at')
        updated_at = request.POST.get('updated_at')
        context = Product.objects.create(name=name, description=description, category_id=category, created_at=created_at, updated_at=updated_at)
        return render(request, 'catalog/product_add.html', context)

    return render(request, 'catalog/product_add.html')

# def add_product(request):
#     return render(request, 'catalog/product_add.html')