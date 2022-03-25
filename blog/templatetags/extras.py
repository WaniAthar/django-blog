from django import template

register = template.Library()
"""
This is the custom filter i have created, to return the values of the keys in the template

"""
@register.filter(name='get_val')
def get_val(dict, key):
    # return dict[key] this didnt work if the key is empty or not in database
    # so i will return
    return dict.get(key)