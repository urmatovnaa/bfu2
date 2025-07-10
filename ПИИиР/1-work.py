surname = input('Как ваша фамилия?')
name = input('Как ваше имя?')
degree = bool(int(input("Вы Магистр или Бакалавр?\nВведите 1-Магистр, 0-Бакалавр")))
field_of_study = input("На каком направлении подготовки вы обучаетесь?")
course_number = int(input('На каком курсе вы обучаетесь?'))
if degree:
    year_of_admission = 2021 - course_number
    year_of_graduation = 2027 - course_number
else:
    year_of_admission = 2025 - course_number
    year_of_graduation = 2029 - course_number
print(f'''
Уважаемый(ая) {surname} {name}, мы очень рады, что вы поступили к нам в университет в {year_of_admission} году на {field_of_study}.
Сейчас вы обучаетесь на {course_number} курсе. В случае успешного обучения вы получите диплом в {year_of_graduation} году.
Спасибо за ичпользование нашей программы. До новых встреч.
''')