# Проект FitLife - MVP версия 1.0


# 1. Знакомство
# TODO: Спроси у пользователя имя и сохрани в переменную user_name
# TODO: Спроси возраст и сохрани в переменную user_age (не забудь преобразовать
# в число)
def user_name():
    """Функция для запроса имени пользователя с проверкой
    на корректность ввода
    """
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


def user_age():
    """Функция для запроса возраста пользователя с проверкой ввода"""
    user_age = input("Сколько вам полных лет? ")
    if user_age.strip() == "":
        print("Ошибка: возраст не может быть пустым.")
        return user_age()
    elif not user_age.isdigit():
        print("Ошибка: возраст должен быть числом.")
        return user_age()
    user_age = int(user_age)
    if user_age < 0 or user_age > 125:
        print("Ошибка: возраст не может быть отрицательным или превышать 125.")
        return user_age()
    else:
        print(f"Спасибо! Ваш возраст: {user_age} лет.")
        return user_age


# 2. Сбор данных
# TODO: Запроси вес (в кг) и сохрани в user_weight (тип float)
# TODO: Запроси рост (в метрах, например 1.75) и сохрани в user_height
# (тип float)
def user_weight():
    """Функция для запроса веса пользователя
    с проверкой на корректность ввода
    """
    while True:
        user_weight = input("Введите ваш вес в килограммах, используя точку,"
                            " например 70.5: ")
        if user_weight.strip() == "":
            print("Ошибка: вес не может быть пустым.")
            continue
        elif not user_weight.replace('.', '', 1).isdigit():
            print("Ошибка: вес должен быть числом.")
            continue
        user_weight = float(user_weight)
        user_weight = round(user_weight, 2)
        if user_weight <= 0 or user_weight > 400:
            print("Ошибка: вес должен быть положительным числом "
                  "и не превышать 400 кг.")
            continue
        else:
            print(f"Спасибо! Ваш вес: {user_weight} кг.")
            break
    return user_weight


# Функция для запроса роста пользователя с проверкой на корректность ввода
def user_height():
    """Функция для запроса роста пользователя
    с проверкой на корректность ввода
    """
    while True:
        user_height = input("Введите рост в метрах, используя точку,"
                            "например 1.75: ")
        if user_height.strip() == "":
            print("Ошибка: рост не может быть пустым.")
            continue
        elif not user_height.replace('.', '', 1).isdigit():
            print("Ошибка: рост должен быть числом.")
            continue
        user_height = float(user_height)
        user_height = round(user_height, 2)
        if user_height <= 0 or user_height > 2.50:
            print("Ошибка: рост должен быть положительным числом"
                  " и не превышать 2.50")
            continue
        else:
            print(f"Спасибо! Ваш рост: {user_height} м.")
            break
    return user_height


# 3. Логика расчетов (Функции как "черный ящик": используем арифметику)
# Формула ИМТ: вес разделить на (рост в квадрате)
# TODO: Рассчитай bmi (Индекс массы тела)
def user_bmi(user_weight, user_height):
    """Функция для расчета индекса массы тела (BMI)
    с проверкой согласия пользователя
    """
    agreement = input("Хотите рассчитать ваш индекс массы тела (BMI)?"
                      " (да/нет): ").strip().lower()
    if agreement == "да":
        # расчёт индекса массы тела
        bmi = user_weight / (user_height ** 2)
        return round(bmi, 1)
    else:
        print("Хорошо расчет BMI будет пропущен.")


# Подсчет воды: вес * 30 мл
# TODO: Рассчитай water_needed
def user_water_intake(user_weight):
    """Функция для расчета суточной нормы потребления воды
    с проверкой согласия пользователя
    """
    agreement = input("Хотите рассчитать вашу суточную норму потребления воды?"
                      "(да/нет): ").strip().lower()
    if agreement == "да":
        WATER_PER_KG = 30
        # расчёт нормы потребления воды
        water_ml = user_weight * WATER_PER_KG
        # Конвертация из миллилитров в литры
        water_l = water_ml / 1000
        return round(water_l, 3)
    else:
        print("Хорошо расчет нормы потребления воды будет пропущен.")


# 4. Вывод красивого результата
# TODO: Используй f-строку, чтобы вывести приветствие
# TODO: Выведи возраст, ИМТ (округленный до 1 знака) и норму воды.
def report_user_data(name, age, weight, user_height, bmi, water_l):
    """Функция для вывода отчета с данными пользователя"""
    print("\n----- Ваши данные -----")
    print(f"Отчет для пользователя: {name}, ({age}) л.")
    print(f"Вес: {weight} кг")
    print(f"Рост: {user_height} м")
    if bmi is not None:
        print(f"Твой Индекс Массы Тела: {bmi:.1f}")
    else:
        print("BMI: расчет пропущен")
    if water_l is not None:
        print(f"Рекомендуемая норма воды: {water_l:.3f} л")
    else:
        print("Суточная норма потребления воды: расчет пропущен")
    print("Расчет окончен. Будьте здоровы!")


user_name = user_name()
user_age = user_age()
weight = user_weight()
height = user_height()
bmi = user_bmi(weight, height)
water_l = user_water_intake(weight)
report_user_data(user_name, user_age, weight, height, bmi, water_l)
