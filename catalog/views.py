from django.shortcuts import render





def home(request):
    return render(request, 'catalog/home.html')


def contacts(request):
    if request.method == 'POST':
        with open('catalog/text.txt', 'a', encoding='utf-8') as file:
            name = request.POST.get('name')
            phone = request.POST.get('phone')
            message = request.POST.get('message')
            file.write(f"Имя пользователя : {name}\nТелефон: {phone}\nСообщение: {message}\n")
            print(f"Имя пользователя : {name}\nТелефон: {phone}\nСообщение: {message}\n")


    return render(request, 'catalog/contacts.html')
