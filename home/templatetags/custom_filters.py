from django import template

register = template.Library()

@register.filter
def last_n_chars(value, n):
    """Return the last n characters of the string."""
    if isinstance(value, str):
        return value[-n:]
    else:
        return str(value)[-n:].upper()
