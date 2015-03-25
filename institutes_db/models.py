import datetime

from django.db import models

YEAR_CHOICES = []
for r in range(1900, (datetime.datetime.now().year+1)):
    YEAR_CHOICES.append((r,r))

# Identification section
class College(models.Model):
    college_name = models.CharField(max_length=45)

# Contact & Information section
class Contact(models.Model):
    college = models.ForeignKey(College)
    contact_name = models.CharField(max_length=45)
    ph_no = models.BigIntegerField(max_length=10)

class Address(models.Model):
    college = models.ForeignKey(College)
    address = models.CharField(max_length=45)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)

class State(models.Model):
    state_name = models.CharField(max_length=45)

class City(models.Model):
    city_name = models.CharField(max_length=45)

class Located_at(models.Model):
    city = models.ForeignKey(City)
    state = models.ForeignKey(State)
    college = models.ForeignKey(College)

class Web_Links(models.Model):
    college = models.ForeignKey(College)
    web_page = models.CharField(max_length=45)
    wiki_link = models.CharField(max_length=45)
    fb_page = models.CharField(max_length=45)

# Academics section
class Course(models.Model):
    course_name = models.CharField(max_length=45)

class Department(models.Model):
    dept_name = models.CharField(max_length=45)

class Qualifying_Examination(models.Model):
    exam_name = models.CharField(max_length=45)

class Degree(models.Model):
    degree_name = models.CharField(max_length=45)

class Offers(models.Model):
    college = models.ForeignKey(College)
    dept = models.ForeignKey(Department)
    degree = models.ForeignKey(Degree)
    course = models.ForeignKey(Course)
    exam = models.ForeignKey(Qualifying_Examination)

    class Meta:
        unique_together = (("college", "dept", "degree", "course"),)

# History & Statistics
class Offer_Statistics(models.Model):
    offers = models.ForeignKey(Offers)
    annual_fee = models.IntegerField(null=True)
    students_admitted = models.PositiveIntegerField(null=True)
    year = models.IntegerField(max_length=4, choices=YEAR_CHOICES)

    class Meta:
        unique_together = (("offers", "year",),)

class Board(models.Model):
    board_name = models.CharField(max_length=45)

class Approves(models.Model):
    college = models.ForeignKey(College)
    board = models.ForeignKey(Board)

    class Meta:
        unique_together = (("college", "board"),)

class Founding_History(models.Model):
    college = models.ForeignKey(College)
    founder_name = models.CharField(max_length=45)
    founding_year = models.IntegerField(max_length=4, choices=YEAR_CHOICES)
