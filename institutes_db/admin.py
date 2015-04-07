from django.contrib import admin

# Register your models here.
from .models import Address, Approves, Board, City, College, Contact, Course, Degree, Department, Founding_History, Located_at, Offer_Statistics, Offers, Qualifying_Examination, State, Web_Links

admin.site.register(Address)
admin.site.register(Approves)
admin.site.register(Board)
admin.site.register(City)
admin.site.register(College)
admin.site.register(Contact)
admin.site.register(Course)
admin.site.register(Degree)
admin.site.register(Department)
admin.site.register(Founding_History)
admin.site.register(Located_at)
admin.site.register(Offer_Statistics)
admin.site.register(Offers)
admin.site.register(Qualifying_Examination)
admin.site.register(State)
admin.site.register(Web_Links)
