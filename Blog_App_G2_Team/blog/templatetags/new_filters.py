from django import template

register = template.Library() 

@register.filter(name='is_viewer') 
def is_viewer(user):
    return user.groups.filter(name='User-Group').exists() 

@register.filter(name='is_admin') 
def is_admin(user) :
    return user.groups.filter(name='Admin-Group').exists() 

@register.filter(name='category') 
def category (categories , category) :
    return categories[category] 