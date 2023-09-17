from Knagu.models import Student
from SERVICES.CheckStudent import check_student_exist

def addStudent(name_student,group):
    """
    Сервис добавляет нового студента в БД
    Вход: имя, группа
    Выход: добавление в Бд

    """

    if not (check_student_exist(name=name_student, group=group)):
        student_info = Student(
            name=name_student,
            group=group,
        )
        student_info.save()