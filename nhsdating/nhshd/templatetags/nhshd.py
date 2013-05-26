from django import template


register = template.Library()

@register.simple_tag(takes_context=True)
def inbox_count(context):
    user = context['request'].user
    count = user.received_messages.filter(read_flag=False).distinct('sender').count()
    if count:
        return "(%s)" % count
    else:
        return ""

