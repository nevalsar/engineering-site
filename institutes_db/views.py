from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from institutes_db.models import Address, Approves, Board, City, College, Contact, Course, Degree, Department, Founding_History, Located_at, Offer_Statistics, Offers, Qualifying_Examination, State, Web_Links

def index(request):
    return render(request, 'institutes_db/index.html')

def table(request, profile_name=None):
    located = Located_at.objects.all()
    if profile_name in ["student", "faculty", "college", "recruiter", "analyst"]:
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
        return render(request, 'institutes_db/table.html', {
                'located': located,
                })

def college(request, id=None):
    if id is not None:
        college = get_or_none(College, pk=id)
        address = get_or_none(Address, college=id)
        contact = get_or_none(Contact, college=id)
        located = get_or_none(Located_at, college=id)
        links = get_or_none(Web_Links, college=id)
        return render(request, 'institutes_db/college.html', {
            'college': college,
            'address': address,
            'contact': contact,
            'located': located,
            'links': links,
            })
    else:
        return render(request, 'institutes_db/college.html')

def get_or_none(classmodel, **kwargs):
    try:
        return classmodel.objects.get(**kwargs)
    except classmodel.DoesNotExist:
        return None
