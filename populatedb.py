import os
import csv
import django

os.environ["DJANGO_SETTINGS_MODULE"] =  "engineering_site.settings"
django.setup()
from institutes_db.models import Address, Approves, Board, City, College, Contact, Course, Degree, Department, Founding_History, Located_at, Offer_Statistics, Offers, Qualifying_Examination, State, Web_Links

# Don't change the stuff above

with open('dbms-state.csv', 'rb') as csvfile:
	datareader = csv.reader(csvfile, delimiter=',')
	for row in datareader:
		temp = State(state_name=row[0].strip())
		temp.save()

with open('dbms-city.csv', 'rb') as csvfile:
	datareader = csv.reader(csvfile, delimiter=',')
	for row in datareader:
		temp = City(city_name=row[0].strip())
		temp.save()

with open('dbms-board.csv', 'rb') as csvfile:
	datareader = csv.reader(csvfile, delimiter=',')
	for row in datareader:
		temp = Board(board_name=row[0].strip())
		temp.save()

with open('dbms-data1.csv', 'rb') as csvfile:
	datareader = csv.reader(csvfile, delimiter=',')
	for row in datareader:
		#print row[0].strip()
		temp = College(college_name=row[0].strip())
		temp.save()



with open('dbms-course_name.csv', 'rb') as csvfile:
	datareader = csv.reader(csvfile, delimiter=',')
	for row in datareader:
		temp = Course(course_name = row[0].strip())
		temp.save()
		temp = Department(dept_name = row[0].strip())
		temp.save()



with open('dbms-exam.csv', 'rb') as csvfile:
	datareader = csv.reader(csvfile, delimiter=',')
	for row in datareader:
		temp = Qualifying_Examination( exam_name = row[0].strip())
		temp.save()

with open('dbms-degree.csv', 'rb') as csvfile:
	datareader = csv.reader(csvfile, delimiter=',')
	for row in datareader:
		temp = Degree( degree_name = row[0].strip())
		temp.save()




		


#temp=College(college_nam
# Sample object creation syntax


# If a table has foreign keys, use the following syntax

# print College.objects.all()

# If a table has foreign keys, use the following syntax
# temp = Approves()
# temp.college = College.objects.get(college_name="IIT")
# temp.board = Board.objects.get(board_name="CBSE")
# temp.save()
