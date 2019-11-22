from django import template

register = template.Library()


@register.simple_tag
def get_price(amount, price, extra_amount):
    extra_price = 0.5
    return "%.2f" % (float(amount*price) + (extra_amount * extra_price * amount))


@register.simple_tag
def get_total_price(items):
    extra_price = 0.5
    total = 0
    for item in items:
        extra_amount = len(item.extras.all())
        total += float(item.quantity * item.product.price) + (extra_amount * extra_price * item.quantity)
    return "%.2f" % total
