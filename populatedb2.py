import os
import csv
import django

os.environ["DJANGO_SETTINGS_MODULE"] =  "engineering_site.settings"
django.setup()
from institutes_db.models import Address, Approves, Board, City, College, Contact, Course, Degree, Department, Founding_History, Located_at, Offer_Statistics, Offers, Qualifying_Examination, State, Web_Links



with open('data/dbms-data1.csv', 'rb') as csvfile:
    datareader = csv.reader(csvfile, delimiter=',')
    for row in datareader:
        print row[4]
        temp1 = City.objects.get(city_name=row[3])
        temp2 = State.objects.get(state_name=row[4])
        temp3 = College.objects.get(college_name = row[0])
        Located_at.objects.create(city = temp1, state=temp2, college=temp3)

        temp1 = College.objects.get(college_name = row[0])
        temp2 = row[9]
        temp3 = row[10]
        temp4 = row[11]
        Address.objects.create(college = temp1,address=temp2,latitude=temp3,longitude=temp4)


        temp1 = College.objects.get(college_name = row[0])
        temp2= row[5]
        temp3= row[6]
        Contact.objects.create(college = temp1, contact_name=temp2, ph_no=temp3)


        temp1 = College.objects.get(college_name = row[0])
        temp2 = row[12]
        Web_Links.objects.create(college = temp1, web_page=temp2)

        temp1 = College.objects.get(college_name = row[0])
        temp2 = row[14]
        temp3 = row[15]
        Founding_History.objects.create(college = temp1, founder_name = temp2, founding_year = temp3)

        temp1 = College.objects.get(college_name = row[0])
        print row[1]
        temp2 = Board.objects.get(board_name = row[1])
        print temp2
        Approves.objects.create(college = temp1, board = temp2)

i=1

with open('data/dbms-Offer.csv', 'rb') as csvfile:
    datareader = csv.reader(csvfile, delimiter=',')
    for row in datareader:
        temp1 = College.objects.get(pk = row[1])
        temp2 = Department.objects.get(pk = row[3])
        temp3 = Degree.objects.get(pk = row[2])
        temp4 = Course.objects.get(pk = row[4])
        temp5 = Qualifying_Examination.objects.get(pk = row[5])
        Offers.objects.create(college = temp1, dept = temp2, degree = temp3, course = temp4, exam = temp5)
        i=i+1
        if i==69:
            break
'''
i=1


with open('data/dbms-Offer_Statistics.csv', 'rb') as csvfile:
    datareader = csv.reader(csvfile, delimiter=',')
    for row in datareader:
        temp1 = Offers.objects.get(pk = row[0])
        temp2 = row[1]
        temp3 = row[2]
        temp4 = row[3]
        print i
        Offer_Statistics.objects.create(offers = temp1, annual_fee=temp2, students_admitted=temp3, year=temp4)
        if i==20:
            break

'''
