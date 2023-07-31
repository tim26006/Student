from Knagu.models import Student

def check_student_exist(name,group):
    """
        Сервис проверяет, есть ли уже студент в БД
    """
    try:

        student = Student.objects.get(name=name,group=group)
        return True
    except Student.DoesNotExist:
        return False