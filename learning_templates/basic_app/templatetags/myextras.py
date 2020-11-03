from django import template

register = template.Library()

@register.filter(name = 'cut')
def cut(value,arg):
    
    """ 
    This will cuts out all the value of "args" from the string
    """
    return value.replace(arg,"")