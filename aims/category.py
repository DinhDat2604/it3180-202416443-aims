def search_by_category(items, category):
    return [dvd for dvd in items if dvd.category.lower() == category.lower()]