import os
os.environ["DJANGO_SETTINGS_MODULE"] =  "engineering_site.settings"

from institutes_db.models import Address, Approves, Board, City, College, Contact, Course, Degree, Department, Founding_History, Located_at, Offer_Statistics, Offers, Qualifying_Examination, State, Web_Links

# Don't change the stuff above

# Sample object creation syntax
temp = State(state_name="Kerala")
temp.save()

# If a table has foreign keys, use the following syntax
temp = Board(board_name="CBSE")
temp.save()

temp = College(college_name="IIT")
temp.save()

# If a table has foreign keys, use the following syntax
temp = Approves()
temp.college = College.objects.get(college_name="IIT")
temp.board = Board.objects.get(board_name="CBSE")
temp.save()
