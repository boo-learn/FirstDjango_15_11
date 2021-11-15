from django.shortcuts import render, HttpResponse, Http404


items = [
   {"id": 1, "name": "Кроссовки abibas"},
   {"id": 2, "name": "Куртка кожаная"},
   {"id": 3, "name": "Coca-cola 1 литр"},
   {"id": 4, "name": "Картофель фри"},
   {"id": 5, "name": "Кепка"},
]
user = {
    "name": "Евгений",
    "surname": "Юрченко",
    "middlename": "Витальевич",
    "phone": "+7-900-800-11-22",
    "email": "eyurchenko@specialist.ru",
}


def home(request):
    return HttpResponse("<h1>Welcome, home page</h1>")


def about(request):
    result = f"""
        Имя: <b>{user['name']}</b><br>
        Отчество: {user['middlename']}<br>
        Фамилия: Иванов<br>
        телефон: {user['phone']}<br>
        email: vasya@mail.ru<br>
    """
    return HttpResponse(result)


def get_item(request, id):
    for item in items:
        if item["id"] == id:
            return HttpResponse(f"<h2>{item['name']}</h2>")

    raise Http404


def items_list(request):
    result = "<ol>"
    for item in items:
        result += f"<li>{item['name']}</li>"
    result += "</ol>"
    return HttpResponse(result)