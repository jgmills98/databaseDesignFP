from django import template

register = template.Library() 

@register.filter(name='groupCheck') 
def groupCheck(user, group_name):
    return user.groups.filter(name=group_name).exists() 