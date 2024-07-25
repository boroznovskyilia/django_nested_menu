def get_children_list(menu):
    return [child for child in menu.children.all()]

def form_final_menus(result_menus,menus,tree_depth,current_url,max_tree_depth):
    if tree_depth > max_tree_depth:
        return
    
    searched_url = "/".join(current_url[:tree_depth+1])
    for menu in menus:
        result_menus.append(menu)
        if menu.url == searched_url:
            menu_children = get_children_list(menu)
            form_final_menus(result_menus,menu_children,tree_depth+1,current_url,max_tree_depth)

    return result_menus

def create_clean_url(request):
    current_url = request.path.strip('/').split('/')
    menu_part_index = current_url.index('menus')
    current_url = current_url[menu_part_index+1:]
    return current_url


def group_menus(menu_items):
    grouped_menus = {}
    for item in menu_items:
        if item.tree_depth not in grouped_menus:
            grouped_menus[item.tree_depth] = []
        grouped_menus[item.tree_depth].append(item)
    return grouped_menus