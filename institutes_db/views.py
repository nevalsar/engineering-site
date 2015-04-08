from django.shortcuts import render, HttpResponse
from django.template import RequestContext, loader

def index(request):
    # template = loader.get_template('institutes_db/index.html')
    # context = RequestContext(request)
    # return HttpResponse(template.render(context))
    return render(request, 'institutes_db/index.html')
