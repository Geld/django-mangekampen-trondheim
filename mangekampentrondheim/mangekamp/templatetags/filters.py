from django import template
from mangekampentrondheim.settings import STATIC_URL
register = template.Library()

@register.filter("has_user")
def has_user(event, user):
    return user in event.participants

@register.filter("to_mangekjemper_status")
def to_mangekjemper_status(season, values):
    required_events = season.required_events
    required_categories = season.required_categories
    future_events = season.get_future_events()
    future_categories = set([e.category for e in future_events])
    for c in values['categories']:
        if c not in future_categories:
            future_categories.add(c)

    if values['attendance'] >= required_events and len(values['categories']) >= required_categories:
        return '<img src="{0}img/mangekjemper_done.png" style="width:30px; height:30px;"></img>'.format(STATIC_URL)
    if values['attendance'] + len(future_events) >= required_events and len(future_categories) >= required_categories:
        return '<img src="{0}img/mangekjemper_yes.png" style="width:30px; height:30px;"></img>'.format(STATIC_URL)
    else:
        return '<img src="{0}img/mangekjemper_no.png" style="width:30px; height:30px;"></img>'.format(STATIC_URL)

@register.filter("category_to_style")
def category_to_style(category):
    if category == 1: return "background-color:#FF668C;"
    if category == 2: return "background-color:#C6FFB3;"
    if category == 3: return "background-color:#809FFF;"
    return ""

@register.filter("category_tag")
def category_tag(category):
    if category == 1: return '&nbsp;&nbsp;<span class="label label-important">T</span>'
    if category == 2: return '&nbsp;&nbsp;<span class="label label-success">U</span>'
    if category == 3: return '&nbsp;&nbsp;<span class="label label-info">B</span>'
    return ""
