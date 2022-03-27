from django import template


register = template.Library()


@register.filter(name='calc_itemtotal')
def calc_itemtotal(price, quantity):
    return price * quantity
