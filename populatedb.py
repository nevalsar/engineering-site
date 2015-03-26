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
		temp = State(state_name=row[0])
		temp.save()

with open('dbms-city.csv', 'rb') as csvfile:
	datareader = csv.reader(csvfile, delimiter=',')
	for row in datareader:
		temp = City(city_name=row[0])
		temp.save()

with open('dbms-board.csv', 'rb') as csvfile:
	datareader = csv.reader(csvfile, delimiter=',')
	for row in datareader:
		temp = Board(board_name=row[0])
		temp.save()

with open('dbms-data1.csv', 'rb') as csvfile:
	datareader = csv.reader(csvfile, delimiter=',')
	for row in datareader:
		#print row[0]
		temp = College(college_name=row[0])
		temp.save()
		tempobj = College.objects.get(college_name=row[0])
		id = tempobj.pk
		print id
		temp = City.objects.get(city_name=row[4])
		Located_at.objects.create(city = temp)
		temp.save()

		temp = State.objects.get(state_name=row[5])
		Located_at.objects.create(state = temp)
		temp.save()

		temp = College.objects.get(college_name = row[0])
		Located_at.objects.create(college = temp)
		temp.save()

		temp = College.objects.get(college_name = row[0])
		Address.objects.create(college = temp)
		temp.save()

		temp = Address(address = row[9])
		temp.save()
		temp = Address(latitude = row[10])
		temp.save()
		temp = Address(longitude = row[11])
		temp.save()
		temp = College.objects.get(college_name = row[0])
		Contact.objects.create(college = temp)
		temp.save()

		temp= Contact(contact_name = row[5])
		temp.save()
		temp= Contact(ph_no= row[6])
		temp.save()

		temp = College.objects.get(college_name = row[0])
		Web_Links.objects.create(college = temp)
		temp.save()
		temp = Web_Links(web_page = row[12])
		temp.save()
		temp = College.objects.get(college_name = row[0])
		Founding_History.objects.create(college = temp)
		temp.save()
		temp = Founding_History(founder_name = row[14])
		temp.save()
		temp = Founding_History(founding_year = row[15])
		temp.save()
		temp = Board(board_name = row[1])
		temp.save()
		temp = College.objects.get(college_name = row[0])
		Approves.objects.create(college = temp)
		temp.save()
		temp = Board.objects.get(board_name = row[0])
		Approves.objects.create(board = temp)
		temp.save()

with open('dbms-course_name.csv', 'rb') as csvfile:
	datareader = csv.reader(csvfile, delimiter=',')
	for row in datareader:
		temp = Course(course_name = row[0])
		temp.save()
		temp = Department(dept_name = row[0])
		temp.save()



with open('dbms-exam.csv', 'rb') as csvfile:
	datareader = csv.reader(csvfile, delimiter=',')
	for row in datareader:
		temp = Qualifying_Examination( exam_name = row[0])
		temp.save()

with open('dbms-degree.csv', 'rb') as csvfile:
	datareader = csv.reader(csvfile, delimiter=',')
	for row in datareader:
		temp = Degree( degree_name = row[0])
		temp.save()


with open('dbms-Offer.csv', 'rb') as csvfile:
	datareader = csv.reader(csvfile, delimiter=',')
	for row in datareader:
		temp = College.objects.get(pk = row[0])
		Offers.objects.create(college = temp)
		temp.save()
		temp = Department.objects.get(pk = row[1])
		Offers.objects.create(dept = temp)
		temp.save()
		temp = Degree.objects.get(pk = row[2])
		Offers.objects.create(degree = temp)
		temp.save()
		temp = Course.objects.get(pk = row[3])
		Offers.objects.create(course = temp)
		temp.save()
		temp = Qualifying_Examination.objects.get(pk = row[4])
		Offers.objects.create(exam = temp)
		temp.save()

with open('dbms-Offer_Statistics.csv', 'rb') as csvfile:
	datareader = csv.reader(csvfile, delimiter=',')
	for row in datareader:
		temp = Offers.objects.get(pk = row[0])
		Offer_Statistics.objects.create(course = temp)
		temp.save()
		temp = Offer_Statistics(annual_fee = row[1])
		temp.save()
		temp = Offer_Statistics(students_admitted=row[3])
		temp.save()
		temp = Offer_Statistics(year=row[4])
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
