from django import template
register=template.Library()

@register.filter(name='is_in_cart')
def product_in_cart(x , cart):
    keys=cart.keys()
    for k in keys:
        if int(k) == x.id:
            return True
    return False


@register.filter(name='count_cart')
def count_cart(x , cart):
    keys=cart.keys()
    for k in keys:
        if int(k) == x.id:
            return cart.get(k)
    return 0

@register.filter(name='total_price')
def total_price(x , cart):
    return x.price * count_cart(x, cart)

@register.filter(name='total')
def total(product_data, cart):
    sum=0
    for x in product_data:
        sum = sum + total_price(x, cart)
    
    return sum

@register.filter(name='currency')
def currency(number):
    return "Rs. " + str(number)


@register.filter(name='multiply')
def multiply(number,numberone):
    return number * numberone

@register.filter(name='addcartvalues')
def addcartvalues(cart):
    v=cart.values()
    sum=0
    for x in v:
        sum = sum + x
    return sum
