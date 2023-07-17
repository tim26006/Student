
from collections import defaultdict
import os


def GetDir():
    subjects = defaultdict(list)
    # определение текущей рабочей директории
    path = "/Users/timofeymac/PycharmProjects/Student/StudentHelper/Knagu/static/subject_templates"
    # чтение записей
    with os.scandir(path) as listOfEntries:

        for entry in listOfEntries:
            if entry.is_file() and not(entry.name == "sample.docx") :
                sub = entry.name.split("-")[0]
                p = os.path.abspath(entry.name)
                file_url = str(entry.name)
                subjects[sub].append({"type": entry.name.split("-")[1],"path":file_url})


    return subjects

