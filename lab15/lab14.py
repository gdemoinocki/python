from sqlalchemy import create_engine

import src.database as db

engine = create_engine('sqlite:///sqlite3.db')
# db.session.configure(bind=engine)
print(
    """
1. Добавить преподавателя
2. Добавить кафедру
3. Добавить должность
4. Все преподаватели
5. Все кафедры

0. Выход
"""
)
while True:

    req = input("\nВыбор действия: ")

    if req == "1":
        fio = input("  ФИО: ")
        date_of_br = input("  Дата рождения: ")
        dep_id = input(' id кафедры')
        post_id = input(' id должности ')

        db.add_teacher(fio, date_of_br, dep_id, post_id)

    elif req == "2":
        name = input("  Название кафедры: ")
        institute = input(" Название института ")

        db.add_department(name, institute)

    elif req == "3":
        name= input("  Название должности: ")

        db.add_post(name)

    elif req == "4":
        teachers = db.all_teacher()

        if not teachers:
            print("  Пока пусто")

        for teachers_id, data in teachers.items():
            print(f"  {teachers_id} ")
            print(f"    ФИО: {data['fio']}")
            print(f"    Дата рождения: {data['date_of_br']}")
            print(f"    Название кафедры: {data['deppartment_name']}")
            print(f"    Должность: {data['post_name']}")

    elif req == "5":
        departments = db.all_departments()

        if not departments:
            print("  Пока пусто")

        for department_id, data in departments.items():
            print(f"  {department_id}.  ")
            print(f"  {data['name']}, Количество преподавателей: {data['count_teachers']} ")

    elif req == "0":
        exit()

    else:
        print("Введена неверная команда")
