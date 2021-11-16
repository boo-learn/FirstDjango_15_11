from django.shortcuts import render, HttpResponse, Http404

items = [
    {"id": 1, "name": "Кроссовки abibas", "quantity": 5},
    {"id": 2, "name": "Куртка кожаная", "quantity": 2},
    {"id": 3, "name": "Coca-cola 1 литр", "quantity": 12},
    {"id": 4, "name": "Картофель фри", "quantity": 0},
    {"id": 5, "name": "Кепка", "quantity": 124},
]

user = {
    "name": "Артём",
    "last_name": "Мовланов"
}


def home(request):
    return render(request, 'index.html', user)


def about(request):
    html_text = "Имя: <b>Иван</b><br>Отчество: <b>Петрович</b><br>Фамилия: <b>Иванов</b><br>телефон: " \
                "<b>8-923-600-01-02</b><br>email: <b>vasya@mail.ru</b>"
    return HttpResponse(html_text)


def get_items(request, id):
    for item in items:
        if item['id'] == id:
            context = {
                "item": item
            }
            return render(request, 'item.html', context)
    raise Http404



def get_items_list(request):
    context = {
        "items": items
    }
    return render(request, 'items_list.html', context)
