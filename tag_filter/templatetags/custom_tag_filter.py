from django import template

from tag_filter.models import Product

register = template.Library()


@register.filter()
def r_underline(value, length: int):
    """returns a string of given length after substituting a underline in left side of original string"""
    s = value
    if type(value) is not str:
        s = str(value)
    return s.rjust(length, '_')


@register.filter()
def ban_words_with_char_combination(value):
    """in original string bans words with popular char-combinations"""
    char_combinations = ['en', 'al', 'es', 'ac', 'an', 'on']
    s = value
    if type(value) is str:
        s_list = s.replace(',', ' ').split()
        for i in range(len(s_list)):
            if any(map(s_list[i].__contains__, char_combinations)):
                s_list[i] = '***'
        s = ','.join(s_list)
    return s


@register.simple_tag
def random_product():
    prod = Product.objects.order_by('?').first()
    return 'Random product: ' + prod.name + ' Supplier: ' + prod.supplier.name
