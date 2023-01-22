### Question 3
# creating tuple for brothers
brothers = ("Yashwanth","Jashwanth")
print("brothers : ", brothers)
# creating tuple for sisters
sisters =  ("supraja","soujanya")
print("sisters : ", sisters)

# creating siblings by adding brothers and sisters
siblings = brothers + sisters
print("siblings : ", siblings)

# length of siblings tuple
len_of_siblings = len(siblings)
print("length of siblings tuple", len_of_siblings)

# adding parents with siblings tuple creating new tuple
family_members = siblings + ("venkat","laxmi")
print("family members : ", family_members)