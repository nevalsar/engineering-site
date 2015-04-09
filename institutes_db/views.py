from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from institutes_db.models import Address, Approves, Board, City, College, Contact, Course, Degree, Department, Founding_History, Located_at, Offer_Statistics, Offers, Qualifying_Examination, State, Web_Links

def index(request):
    return render(request, 'institutes_db/index.html')

def table(request, profile_name=None):
    if profile_name in ["student", "faculty", "college", "recruiter", "analyst"]:
        located = Located_at.objects.all()
        carval = request.GET.getlist('vehicle','')
        if len(carval) > 0:
            return render(request, 'institutes_db/table.html', {
                'profile_name': profile_name,
                'located': located,
                'carval':carval
                })
        else:
            return render(request, 'institutes_db/table.html', {
                'profile_name': profile_name,
                'located': located,
                })
    else:
        return render(request, 'institutes_db/table.html')
