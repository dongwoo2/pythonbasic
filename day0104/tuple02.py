people = [
    ("Alice",30,"F"),
    ("Bob",25,"M"),
    ("Kim",35,"M"),
    ("Jason",28,"M"),
    ("Som",22,"F"),
    ("Micle",29,"M")
]

print(people[2][2])

sorted_people = sorted(people, key = lambda x:x[1])

for person in sorted_people:
    name,age,gender = person
    print(f"{name} is {age} years old and {gender}.")