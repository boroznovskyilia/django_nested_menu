from django import template
from ..models import MenuItem
from .utils.menu_tags_utils import create_clean_url,group_menus,form_final_menus


register = template.Library()

@register.filter(name='get_range') 
def get_range(number):
    return range(number)

@register.inclusion_tag('menu_app/menu.html',takes_context=True)
def draw_menu(context,menu_url):
    current_url = create_clean_url(context["request"])
    tree_depth = len(current_url)
    menu_items = MenuItem.objects.all().order_by('tree_depth')
    grouped_menus = group_menus(menu_items)
    result_menus = []
    result_menus = form_final_menus(result_menus, grouped_menus[0], 0, current_url,tree_depth+1)
    return {
        'result_menus': result_menus,
        'current_url': current_url,
    }

@register.inclusion_tag('menu_app/start_menu.html',takes_context=True)
def draw_start_menu(context):
    request = context['request']
    current_url = request.path

    top_level_items = MenuItem.objects.filter(parent__isnull=True).prefetch_related('children')
    return {
        'top_level_items': top_level_items,
        'current_url': current_url,
    }
