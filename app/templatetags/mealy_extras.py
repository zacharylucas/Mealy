from django import template

register = template.Library()

@register.filter(name='cut')
def cut(value, arg):
    strings = value.split(',')
    if arg == "0":
        return strings[0]
    else:
        return strings[1]
    #return value
