from django.shortcuts import render


def design(request):
    return render(request, 'info/design.html')


def database(request):
    return render(request, 'info/database.html')


def roadmap(request):
    return render(request, 'info/roadmap.html')