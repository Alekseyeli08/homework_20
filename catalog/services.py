from config.settings import CACHE_ENABLED
from catalog.models import Category
from django.core.cache import cache

def get_category_from_cache():
    if not CACHE_ENABLED:
        return Category.objects.all()
    key = 'category_list'
    category = cache.get(key)
    if category is not None:
        return category
    category = Category.objects.all()
    cache.set(key, category)

    return category

