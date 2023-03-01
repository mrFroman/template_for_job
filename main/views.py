from django.shortcuts import render


def base(request, name):
    return render(request, 'main/index.html', {'name': name})


