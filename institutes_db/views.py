from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

def index(request):
    return render(request, 'institutes_db/index.html')

def table(request, profile_name):
    if profile_name in ["student", "faculty", "college", "recruiter", "analyst"]:
        return render(request, 'institutes_db/table.html', {
            'profile_name': profile_name,
            })
    else:
        return HttpResponseRedirect(reverse('institutes_db:index'))
