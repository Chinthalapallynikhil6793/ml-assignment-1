### Question 9

# input number of students
N = int(input("Enter Number of students : "))
# lb to kg conversion value
lbs_to_kg_convertion_value = 0.4536
lbs_weights = []
kg_weights = []

# input all student weights input
for i in range(0,N):
    lbs_weights.append(int(input("Enter student Weight(lbs) : ")))

print("lbs_weights : ",lbs_weights)

# converted weights to kg
for weight in lbs_weights:
    kg_weights.append(round(weight * lbs_to_kg_convertion_value,2))

print("kg_weights : ", kg_weights)
