### Question 2
# Create an empty dictionary called dog
dog = dict()
# Adding data to dog dictionary
dog['name'] = 'puppy'
dog['color'] = 'brown'
dog['breed'] = 'Labrador'
dog['legs'] = 4
dog['age'] = 5
print("dog dictionary : ", dog)
# creating student dictionary with data
student = {
    "first_name": "nikhil",
    "last_name": "chinthalapally",
    "gender": "male",
    "age": 22,
    "marital status": "single",
    "skills": ["python", "machine learning", "java"],
    "country": "United States",
    "city": "overland park",
    "address": "6655 w 141 st apt 3407"
}
print("student dictionary : ", student)
# length of the student dictionary
len_student = len(student)
# skills of the student from the dictionary
skills = student['skills']
# type of skills
print("type of skills :",type(skills))
# updating student skills
student['skills'].extend(["AI"])
print("updated student skills : ", student["skills"])
# keys of student dictionary
print("keys of student dictionary : ", list(student.keys()))
# values of student dictionary
print("values of student dictionary : ", list(student.values()))
