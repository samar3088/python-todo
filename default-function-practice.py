def get_age(year_of_birth,current_year=2023):
    return current_year-year_of_birth


def get_nr_items(items):
    items_len = items.split(',')
    return len(items_len)