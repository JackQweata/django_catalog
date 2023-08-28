from catalog.serives import get_cache_category


def get_site_data(request):
    return {'category_list': get_cache_category()}
