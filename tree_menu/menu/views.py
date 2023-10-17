from django.shortcuts import render


def home(request):
    return render(request, 'menu/main.html')


def show_menu(request, parent_url, menu_url):
    return render(request, 'menu/show_menu.html', {'menu_url': menu_url})