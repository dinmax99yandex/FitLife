# Проект FitLife - MVP версия 1.0


# 1. Знакомство
# TODO: Спроси у пользователя имя и сохрани в переменную user_name
# TODO: Спроси возраст и сохрани в переменную user_age (не забудь преобразовать в число)
def define_user_name():
    while True:
        user_name = input("Здравствуйте! Представьтесь, пожалуйста: ")
         # Удаляем пробелы и проверяем, остались ли только буквы
        if user_name.replace(" ", "").isalpha():
            user_name = user_name.title()
            print(f"Приятно познакомиться, {user_name}!")
            break
        else:
            print("Ошибка: имя должно содержать только буквы и пробелы.")
    return user_name

def define_user_age():           
    user_age = input("Сколько вам полных лет? ")
    if user_age.strip() == "":
        print("Ошибка: возраст не может быть пустым.")
        return define_user_age()
    elif not user_age.isdigit():    
        print("Ошибка: возраст должен быть числом.")
        return define_user_age()
    user_age = int(user_age)
    if user_age < 0 or user_age > 125:
        print("Ошибка: возраст не может быть отрицательным или превышать 125.")
        return define_user_age()
    else:
        print(f"Спасибо! Ваш возраст: {user_age} лет.")
        return user_age

# 2. Сбор данных
# TODO: Запроси вес (в кг) и сохрани в user_weight (тип float)
# TODO: Запроси рост (в метрах, например 1.75) и сохрани в user_height (тип float)


# 3. Логика расчетов (Функции как "черный ящик": используем арифметику)
# Формула ИМТ: вес разделить на (рост в квадрате)
# TODO: Рассчитай bmi (Индекс массы тела)


# Подсчет воды: вес * 30 мл
# TODO: Рассчитай water_needed


# 4. Вывод красивого результата
# TODO: Используй f-строку, чтобы вывести приветствие, например: "Привет, Иван!"
# TODO: Выведи возраст, ИМТ (округленный до 1 знака) и норму воды.
print("Расчет окончен. Будьте здоровы!")