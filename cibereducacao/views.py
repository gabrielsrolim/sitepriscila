from django.shortcuts import render_to_response
from django.http import HttpResponse
import datetime

def hello(request):
    return HttpResponse("Hello world")

def current_datetime(request):
    current_date = datetime.datetime.now()
    #now = datetime.datetime.now()
    return render_to_response('current_datetime.html',locals())

def hours_ahead(request,offset):
    try:
        hour_offset = int(offset)
    except ValueError:
        raise Http404()
    next_time = datetime.datetime.now() + datetime.timedelta(hours=hour_offset)
    return render_to_response('hours_ahead.html',locals())

def display_meta(request):
    values = request.META.items()
    values.sort()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))

