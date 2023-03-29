from django import template
register = template.Library()
@register.filter()
def is_numberic(value):
    try:
        int(value)
        return True

    except:

        return False