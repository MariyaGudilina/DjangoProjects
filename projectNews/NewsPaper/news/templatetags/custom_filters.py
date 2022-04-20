from django import template

register = template.Library()


@register.filter()
def censor(value):

   badWords = ['животное', 'Животное', 'Нацики', 'нацики', 'Киев', 'киев', 'Бойцы']

   """
   value: значение, к которому нужно применить фильтр
   
   """
   for word in badWords:
      value = value.replace(word, word[:1]+'*' * len(word))



   return f'{value}'


