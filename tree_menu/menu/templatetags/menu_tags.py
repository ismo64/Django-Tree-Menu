from django import template
from menu.models import Menu
from django.shortcuts import get_object_or_404

register = template.Library()

@register.inclusion_tag('menu/menu_childs.html')
def draw_menu(menu_name):
    menu = get_object_or_404(Menu, url=menu_name)
    return {'menu': menu}