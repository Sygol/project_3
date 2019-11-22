from orders.models import CartItem
from pizza.models import SubExtra


def if_toppings(product, cleaned_data):
    if cleaned_data.get('toppings'):
        for topping in cleaned_data['toppings']:
            product.toppings.add(topping.id)


def if_extra_cheese(product, cleaned_data):
    if cleaned_data.get('extra_cheese'):
        cheese_id = SubExtra.objects.get(name='Cheese').id
        product.extras.add(cheese_id)


def if_additional_extras(product, cleaned_data):
    if cleaned_data.get('extras'):
        for extra in cleaned_data['extras']:
            product.extras.add(extra)


def create_all_additions(product, cleaned_data):
    if_toppings(product, cleaned_data)
    if_extra_cheese(product, cleaned_data)
    if_additional_extras(product, cleaned_data)


def create_lists_of_toppings_to_remove_and_add(cart_id, cleaned_data):
    new_topping_list = list(cleaned_data['toppings'])
    old_topping_list = list(CartItem.objects.get(id=cart_id).values_list('toppings', flat=True))
    toppings_to_remove = []
    toppings_to_add = []

    for topping in new_topping_list:
        if topping not in old_topping_list:
            toppings_to_add.append(topping)
    for topping in old_topping_list:
        if topping not in new_topping_list:
            toppings_to_remove.append(topping)
    return toppings_to_remove, toppings_to_add


def remove_or_add_toppings(to_remove, to_add, cart_id):
    cart_item = CartItem.objects.filter(id=cart_id).get()
    for topping in to_remove:
        cart_item.toppings.remove(topping)
    for topping in to_add:
        cart_item.toppings.add(topping)


def create_lists_of_extras_to_remove_and_add(cart_id, cleaned_data):
    cheese_id = SubExtra.objects.get(name='Cheese').id
    new_extras_list = []
    extras_to_remove = []
    extras_to_add = []
    old_extras_list = list(CartItem.objects.filter(id=cart_id).values_list('extras', flat=True))

    if cleaned_data.get('extras'):
        new_extras_list = list(cleaned_data['extras'])
    if cleaned_data['extra_cheese']:
        new_extras_list.append(SubExtra.objects.get(id=cheese_id))
    for extra in new_extras_list:
        if extra not in old_extras_list:
            extras_to_add.append(extra)
    for extra in old_extras_list:
        if extra not in new_extras_list:
            extras_to_remove.append(extra)
    return extras_to_remove, extras_to_add


def remove_or_add_extras(to_remove, to_add, cart_id):
    cart_item = CartItem.objects.filter(id=cart_id).get()
    for extra in to_remove:
        cart_item.extras.remove(extra)
    for extra in to_add:
        cart_item.extras.add(extra)


def update_all_additions(cart_id, cleaned_data):
    old_toppings_list = list(CartItem.objects.filter(id=cart_id).values_list('toppings', flat=True))
    old_extras_list = list(CartItem.objects.filter(id=cart_id).values_list('extras', flat=True))
    if cleaned_data.get('toppings') or old_toppings_list:
        to_remove, to_add = create_lists_of_toppings_to_remove_and_add(cart_id, cleaned_data)
        remove_or_add_toppings(to_remove, to_add, cart_id)
    if cleaned_data.get('extras') or cleaned_data.get('extra_cheese') or old_extras_list:
        to_remove, to_add = create_lists_of_extras_to_remove_and_add(cart_id, cleaned_data)
        remove_or_add_extras(to_remove, to_add, cart_id)