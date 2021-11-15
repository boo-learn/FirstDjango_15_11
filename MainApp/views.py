from django.shortcuts import render, HttpResponse


def home(request):
    return HttpResponse("<h1>Welcome, home page</h1>")


def about(request):
    return HttpResponse("Автор: Юрченко Евгений")