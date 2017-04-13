from django import template
from datetime import date

register = template.Library()

@register.filter(name='allowed')
def allowed(born):
    today = date.today()
    age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
    allowed = False if age < 13 else True
    ret = 'allowed' if allowed else 'blocked'
    return ret

@register.filter(name='fizzbuzz')
def fizzbuzz(number):
    ret = ''
    if number % 3 == 0: ret += 'Bizz'
    if number % 5 == 0: ret += 'Fuzz'
    ret = ret if ret else number
    return ret
