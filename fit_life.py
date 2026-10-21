# Проект FitLife - MVP версия 1.0
WATER_PER_KG = 30
INITIAL_AGE = 0
MAX_AGE = 125
INITIAL_WEIGHT = 0
MAX_WEIGHT = 400
INITIAL_HEIGHT = 0
MAX_HEIGHT = 2.50
LITER_TO_ML = 1000


def user_name():
    """Функция для запроса имени пользователя.

    Функция запрашивает имя пользователя и проверяет
    ввод на соответствие, чтобы ввод содержал только
    буквы. Используестя метод isalpha().
    """
    while True:
        user_name = input("Здравствуйте! Представьтесь, пожалуйста: ")
# Удаляем пробелы и проверяем, остались ли только буквы
        if user_name.replace(" ", "").isalpha():
            user_name = user_name.title()
            break
        else:
            print("Ошибка: имя должно содержать только буквы и пробелы.")
    return user_name


def user_age(initial_age, max_age):
    """Функция для запроса возраста пользователя с проверкой ввода.
    
    Функция проверят, чтобы ввод был числом методом isdigit(),
    также ввод не должен быть пустой строкой.
    Возраст не должен быть отрицательным или больше 125 лет.
    Для этого используется условие if с начальным весом initial_age = 0,
    и максимальным весом max_age = 125.
    """
    user_age = input("Сколько вам полных лет? ")
    if user_age.strip() == "":
        print("Ошибка: возраст не может быть пустым.")
        return user_age()
    elif not user_age.isdigit():
        print("Ошибка: возраст должен быть числом.")
        return user_age()
    user_age = int(user_age)
    if user_age < initial_age or user_age > max_age:
        print(f"Ошибка: возраст не может быть отрицательным"
              "или превышать {max_age}.")
        return user_age()
    else:
        return user_age


def user_weight(initial_weight, max_weight):
    """Функция для запроса веса пользователя.

    Функция проверят, чтобы ввод был числом методом isdigit(),
    также ввод не должен быть пустой строкой.
    Вес должен быть положительным числом, не меньше начального веса
    initial_weight = 0 и не превышать максимальный вес max_weight = 400 кг.
    Для этого используется условие if с начальным весом initial_weight,
    и максимальным весом max_weight.
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
        if user_weight <= initial_weight or user_weight > max_weight:
            print(f"Ошибка: вес должен быть положительным числом "
                  "и не превышать {max_weight} кг.")
            continue
        else:
            break
    return user_weight


def user_height(initial_height, max_height):
    """Функция для запроса роста пользователя.

    Функция принимает рост пользователя и первоначально проверяет,
    чтобы пользователь ввел число и не пустую строку.
    Рост должен быть положительным числом типа float
    больше initial_height = 0 и не больше max_height = 2.50 метра.
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
        if user_height <= initial_height or user_height > max_height:
            print(f"Ошибка: рост должен быть положительным числом"
                  " и не превышать {max_height}")
            continue
        else:
            break
    return user_height


def user_bmi(user_weight, user_height):
    """Функция для расчета индекса массы тела (BMI).

    Функция принимает вес пользователя и рост пользователя типа float.
    Args:
        user_weight (float): вес пользователя.
        user_height (float): рост пользователя.

    Returns:
        bmi (float): Индекс массы телы.
    """

    bmi = user_weight / (user_height ** 2)
    return round(bmi, 1)


def user_water_intake(user_weight, water_per_kg, liter_to_ml):
    """Функция для расчета суточной нормы потребления воды.

    Функция принимает вес пользователя и норму потребления воды на
    килограм тела WATER_PER_KG, которая равна 30 мл.
    Расчитывает суточную норму потребления в литрах.
    """
    water_ml = user_weight * water_per_kg
    water_l = water_ml / liter_to_ml
    return round(water_l, 3)


def report_user_data(name, age, weight, height, bmi, water_l):
    """Функция для вывода отчета с данными пользователя."""
    print("\n----- Ваши данные -----")
    print(f"Отчет для пользователя: {name}, ({age}) л.")
    print(f"Вес: {weight} кг")
    print(f"Рост: {height} м")
    if bmi is not None:
        print(f"Твой Индекс Массы Тела: {bmi:.1f}")
    else:
        print("BMI: расчет пропущен")
    if water_l is not None:
        print(f"Рекомендуемая норма воды: {water_l:.3f} л")
    else:
        print("Суточная норма потребления воды: расчет пропущен")
    print("Расчет окончен. Будьте здоровы!")


name = user_name()
age = user_age(INITIAL_AGE, MAX_AGE)
weight = user_weight(INITIAL_WEIGHT, MAX_WEIGHT)
height = user_height(INITIAL_HEIGHT, MAX_HEIGHT)
bmi = user_bmi(weight, height)
water_l = user_water_intake(weight, WATER_PER_KG, LITER_TO_ML)
report_user_data(name, age, weight, height, bmi, water_l)
