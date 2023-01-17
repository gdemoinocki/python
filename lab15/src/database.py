from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session
import models

engine = create_engine('sqlite:///sqlite3.db')
session = Session(bind=engine)

# def add_type_of_control(name):
#     name_toc = session.query(models.Type_of_control).filter(models.Type_of_control.name == name)
#
#     if name_toc.count() != 0:
#         return print("Данный вид контроля уже есть в базе данных")
#
#     new_type = models.Type_of_control(
#         name=name
#     )
#
#     session.add(new_type)
#     session.commit()

def add_post(post_name):
    post = session.query(models.Department).filter(models.Post.name == post_name)

    if post.count() != 0:
        return print("Данная должность уже есть")

    new_depart = models.Department(
        name=post_name,
    )
    session.add(new_depart)
    session.commit()


def add_department(name, ins):
    depart = session.query(models.Department).filter(models.Department.name == name)

    if depart.count() != 0:
        return print("Данная кафедра уже есть")

    new_depart = models.Department(
        name=name,
        institute=ins
    )
    session.add(new_depart)
    session.commit()


def add_teacher(fio, date_of_br, post_id, dep_id):
    depart = session.query(models.Department).filter(models.Department.id == dep_id)

    post = session.query(models.Post).filter(models.Post.id == post_id)


    new_teacher = models.Teacher(
        fio=fio,
        date_of_br=date_of_br,
        department_id=dep_id,
        post_id=post_id
    )
    if depart.count() == 0:
        return print(f'Данная кафедра {dep_id} не найдена')
    elif post.count() == 0:
        return print(f"Данная должность:{post_id} не найдена")

    session.add(new_teacher)
    session.commit()

def all_teacher():
    result = {}

    teachers = session.query(models.Teacher).all()

    for teacher in teachers:
        result[str(teacher.id)] = {
            "fio": teacher.fio,
            "date_of_br": teacher.date_of_br,
        }
        departments = session.query(models.Department).filter(models.Department.id == teachers.department_id)
        for d in departments:
            result[str(teacher.id)].update({
                "deppartment_name": d.name
            })
        possitions = session.query(models.Post).filter(models.Post.id == teachers.post_id)
        for p in possitions:
            result[str(teacher.id)].update({
                "post_name": p.name
            })
    return result


def all_departments():
    result = {}
    departments = session.query(models.Department).all()

    count = 0
    teachers = session.query(models.Teacher).all()

    for d in departments:
        for teacher in teachers:
            if teacher.teacher_id == d.id:
                count += 1

        result[str(d.id)] = {
            "name": d.name,
            "count_teachers": count
        }
        count = 0

    return result

    # def all_types_of_control():
    #     types = session.query(models.Type_of_control).all()
    #
    #     return {str(i.id): i.title for i in types}
