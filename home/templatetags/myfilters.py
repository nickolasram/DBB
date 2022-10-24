from django import template

register = template.Library()

def onlyvalues(dictionary):
    return list(dictionary.values())


register.filter("onlyvalues",onlyvalues)