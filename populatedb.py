import os
import csv
import django

os.environ["DJANGO_SETTINGS_MODULE"] =  "engineering_site.settings"
django.setup()
from institutes_db.models import Address, Approves, Board, City, College, Contact, Course, Degree, Department, Founding_History, Located_at, Offer_Statistics, Offers, Qualifying_Examination, State, Web_Links

# Don't change the stuff above

with open('data/dbms-state.csv', 'rb') as csvfile:
	datareader = csv.reader(csvfile, delimiter=',')
	for row in datareader:
		temp = State(state_name=row[0].strip())
		temp.save()

with open('data/dbms-city.csv', 'rb') as csvfile:
	datareader = csv.reader(csvfile, delimiter=',')
	for row in datareader:
		temp = City(city_name=row[0].strip())
		temp.save()

with open('data/dbms-board.csv', 'rb') as csvfile:
	datareader = csv.reader(csvfile, delimiter=',')
	for row in datareader:
		temp = Board(board_name=row[0].strip())
		temp.save()

with open('data/dbms-data1.csv', 'rb') as csvfile:
	datareader = csv.reader(csvfile, delimiter=',')
	for row in datareader:
		#print row[0].strip()
		temp = College(college_name=row[0].strip())
		temp.save()



with open('data/dbms-course_name.csv', 'rb') as csvfile:
	datareader = csv.reader(csvfile, delimiter=',')
	for row in datareader:
		temp = Course(course_name = row[0].strip())
		temp.save()
		temp = Department(dept_name = row[0].strip())
		temp.save()



with open('data/dbms-exam.csv', 'rb') as csvfile:
	datareader = csv.reader(csvfile, delimiter=',')
	for row in datareader:
		temp = Qualifying_Examination( exam_name = row[0].strip())
		temp.save()

with open('data/dbms-degree.csv', 'rb') as csvfile:
	datareader = csv.reader(csvfile, delimiter=',')
	for row in datareader:
		temp = Degree( degree_name = row[0].strip())
		temp.save()
