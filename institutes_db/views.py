from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from institutes_db.models import Address, Approves, Board, City, College, Contact, Course, Degree, Department, Founding_History, Located_at, Offer_Statistics, Offers, Qualifying_Examination, State, Web_Links

def index(request):
    return render(request, 'institutes_db/index.html')

def table_as_user(request, profile_name):
    if profile_name in ["student", "faculty", "college", "recruiter", "analyst"]:
        colleges = College.objects.all()
        return render(request, 'institutes_db/table.html', {
            'profile_name': profile_name,
            'colleges': colleges,
            })
    else:
        return render(request, 'institutes_db/table.html')

def table_as_guest(request):
    return render(request, 'institutes_db/table.html')
