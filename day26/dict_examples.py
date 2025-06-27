import pandas

# import random

# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]


# student_scores = {student: random.randint(1, 100) for student in names}

# passed_students = {key: value for (key, value) in student_scores.items() if value > 60}

# print(passed_students)


# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

# sentence_list = sentence.split(" ")
# result = {word: len(word) for word in sentence_list}

# print(result)

# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24,
# }

# weather_f = {key: (value * 9 / 5) + 32 for (key, value) in weather_c.items()}

# print(weather_f)

student_dict = {"student": ["Angela", "James", "Lily"], "score": [56, 76, 98]}

student_data_frame = pandas.DataFrame(student_dict)

for index, row in student_data_frame.iterrows():
    print(row.student)
