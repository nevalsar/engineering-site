import datetime

from django.db import models

YEAR_CHOICES = []
for r in range(1900, (datetime.datetime.now().year+1)):
    YEAR_CHOICES.append((r,r))


# Identification section
class College(models.Model):
    college_name = models.CharField(max_length=45)

    def __str__(self):
        return self.college_name


# Contact & Information section
class Contact(models.Model):
    college = models.ForeignKey(College)
    contact_name = models.CharField(max_length=45)
    ph_no = models.BigIntegerField(max_length=10)

    def __str__(self):
        return self.contact_name


class Address(models.Model):
    college = models.ForeignKey(College)
    address = models.CharField(max_length=45)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)

    def __str__(self):
        return self.address

    class Meta:
        verbose_name_plural="Addresses"


class State(models.Model):
    state_name = models.CharField(max_length=45)

    def __str__(self):
        return self.state_name


class City(models.Model):
    city_name = models.CharField(max_length=45)

    def __str__(self):
        return self.city_name

    class Meta:
        verbose_name_plural="Cities"


class Located_at(models.Model):
    city = models.ForeignKey(City)
    state = models.ForeignKey(State)
    college = models.ForeignKey(College)


class Web_Links(models.Model):
    college = models.ForeignKey(College)
    web_page = models.CharField(max_length=45)

    def __str__(self):
        return self.web_page

    class Meta:
        verbose_name_plural="Web_Links"


# Academics section
class Course(models.Model):
    course_name = models.CharField(max_length=45)

    def __str__(self):
        return self.course_name


class Department(models.Model):
    dept_name = models.CharField(max_length=45)

    def __str__(self):
        return self.dept_name


class Qualifying_Examination(models.Model):
    exam_name = models.CharField(max_length=45)

    def __str__(self):
        return self.exam_name


class Degree(models.Model):
    degree_name = models.CharField(max_length=45)

    def __str__(self):
        return self.degree_name


class Offers(models.Model):
    college = models.ForeignKey(College)
    dept = models.ForeignKey(Department)
    degree = models.ForeignKey(Degree)
    course = models.ForeignKey(Course)
    exam = models.ForeignKey(Qualifying_Examination)

    class Meta:
        unique_together = (("college", "dept", "degree", "course"),)
        verbose_name_plural="Offers"


# History & Statistics
class Offer_Statistics(models.Model):
    offers = models.ForeignKey(Offers)
    annual_fee = models.IntegerField(null=True)
    students_admitted = models.PositiveIntegerField(null=True)
    year = models.IntegerField(max_length=4, choices=YEAR_CHOICES)

    class Meta:
        unique_together = (("offers", "year",),)
        verbose_name_plural="Offer_Statistics"


class Board(models.Model):
    board_name = models.CharField(max_length=45)

    def __str__(self):
        return self.board_name


class Approves(models.Model):
    college = models.ForeignKey(College)
    board = models.ForeignKey(Board)

    class Meta:
        unique_together = (("college", "board"),)
        verbose_name_plural="Approves"


class Founding_History(models.Model):
    college = models.ForeignKey(College)
    founder_name = models.CharField(max_length=45)
    founding_year = models.IntegerField(max_length=4, choices=YEAR_CHOICES)

    class Meta:
        verbose_name_plural="Founding_Histories"
