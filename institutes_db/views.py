from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.db.models import Count, Min, Sum, Avg

from institutes_db.models import Address, Approves, Board, City, College, Contact, Course, Degree, Department, Founding_History, Located_at, Offer_Statistics, Offers, Qualifying_Examination, State, Web_Links, Designation, Designated_at

def index(request):
    return render(request, 'institutes_db/index.html')

def table(request, profile_name=None):

    if profile_name in ["student", "faculty", "college", "recruiter", "analyst"]:
        colleges = College.objects.all()

        if "student" in profile_name:
            departments = Department.objects.all();
            degrees = Degree.objects.all();

            deg = request.GET.getlist('deg','')
            dept = request.GET.getlist('dept','')
            if len(deg) > 0:
                deg[:] = (int(x) for x in deg)
            if len(dept) > 0:
                dept[:] = (int(x) for x in dept)

            filterargs = {}
            if len(deg) > 0:
                filterargs = {'offers__degree__in': deg}
            if len(dept) > 0:
                filterargs = {'offers__dept__in': dept}
            print filterargs
            colleges= colleges.filter(**filterargs)
            # colleges= colleges.filter()
            colleges = colleges.annotate(fee = Avg('offers__offer_statistics__annual_fee')).values('college_name','located_at__city__city_name','located_at__state__state_name','fee', 'pk')

            return render(request, 'institutes_db/table.html', {
                'profile_name': profile_name,
                'colleges': colleges,
                'departments': departments,
                'degrees': degrees,
                })

        if "faculty" in profile_name:
            departments = Department.objects.all();
            designations = Designation.objects.all();

            desig = request.GET.getlist('desig','')
            dept = request.GET.getlist('dept','')
            if len(desig) > 0:
                desig[:] = (int(x) for x in desig)
            if len(dept) > 0:
                dept[:] = (int(x) for x in dept)

            print "desig : ", desig
            print "dept : ", dept
            filterargs = {}
            if len(desig) > 0:
                filterargs = {'designated_at__desig__in': desig}
            if len(dept) > 0:
                filterargs = {'designated_at__dept__in': dept}
            print filterargs
            colleges= colleges.filter(**filterargs)
            colleges = colleges.annotate(salary = Avg('designated_at__salary')).values('college_name','located_at__city__city_name','located_at__state__state_name','salary', 'pk')
            print "college", colleges[0]
            return render(request, 'institutes_db/table.html', {
                'profile_name': profile_name,
                'colleges': colleges,
                'departments': departments,
                'designations': designations,
                })

def college(request, id=None):
    if id is not None:
        college = get_or_none(College, pk=id)
        address = get_or_none(Address, college=id)
        contact = get_or_none(Contact, college=id)
        located = get_or_none(Located_at, college=id)
        links = get_or_none(Web_Links, college=id)
        return render(request, 'institutes_db/college.html', {
            'id': id,
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
