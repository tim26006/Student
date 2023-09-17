from django import template
from Knagu.models import Student


register = template.Library()

@register.simple_tag
def get_header_data():
    student = Student.objects.get(name='Сидорин Тимофей')

    student_info = {
        "name": student.name,
        "group": student.group,

    }

    return student_info

