from django.urls import path
from .views import home, show_menu


urlpatterns = [
    path('', home, name='home'),
    path('<slug:parent_url>/<slug:menu_url>/', show_menu, name='show_menu'),
]