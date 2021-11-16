from django.shortcuts import render, HttpResponse, Http404
from django.core.exceptions import ObjectDoesNotExist
from MainApp.models import Item

user = {
    "name": "Артём",
    "last_name": "Мовланов"
}


def home(request):
    context = {
        "user": user,
        "page_title": "Home",
    }
    return render(request, 'index.html', context)


def about(request):
    html_text = "Имя: <b>Иван</b><br>Отчество: <b>Петрович</b><br>Фамилия: <b>Иванов</b><br>телефон: " \
                "<b>8-923-600-01-02</b><br>email: <b>vasya@mail.ru</b>"
    return HttpResponse(html_text)


def get_items(request, id):
    try:
        item = Item.objects.get(id=id)
        context = {
            "page_title": "Страница товара",
            "item": item
        }
        return render(request, 'item.html', context)
    except ObjectDoesNotExist:
        raise Http404


def get_items_list(request):
    items = Item.objects.all()
    context = {
        "page_title": "Список товаров",
        "items": items
    }
    return render(request, 'items_list.html', context)
