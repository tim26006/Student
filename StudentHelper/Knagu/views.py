from django.shortcuts import render
from .forms import Autorization
from SERVICES.RETURN_SUB import *
from SERVICES.titulnikKnagu import *
from SERVICES.GetDir import *
from SERVICES.GptResponse import *
from SERVICES.AddStudent import addStudent
from SERVICES.check_session import session_calculation
from django.http import HttpResponse
stop = 0
new_dict = {}

def index_page(request):
    if request.method == 'POST':
        form = Autorization(request.POST)
    else:
        form = Autorization()
    return render(request, "index.html", {'form': form})



def get_data(request):
    global stop

    if stop == 0:
        form = Autorization(request.POST)
        login = form['login'].value()
        password = form['password'].value()
        global out_info
        out_info = parseLK(username=login, password=password, course=1)
        name_student = out_info["student"]
        group = out_info["group"]
        for item in out_info["marks"]:
            sub = item.split("_")
            if not(sub[1] == "Зачет" or sub[1] == "Экзамен" or sub[1] == "Итоговая оценка"):
                edit_template(sub=sub[0],type_sub=sub[1],group = group)



        addStudent(name_student,group) # добавляем нового студента в бд


    all_subjects_name = GetDir()
    global new_dict

    for key, value_list in all_subjects_name.items():
        new_dict[key] = value_list

    stop = 1
    sesia = out_info["sesia"]
    sesia = session_calculation(str(sesia).strip())
    return render(request, "way.html", {"sesia": sesia})


def way(request):
    sesia = out_info["sesia"]
    sesia = session_calculation(str(sesia).strip())
    return render (request,"way.html", {"sesia":sesia})


def gen(request):
    return render (request,"gen.html")


def list_of_info(request):
    theme = request.POST.get('theme')
    resp = GPTResponse(theme=theme, amount=5)
    return render(request, "list.html", {"theme":resp})


def templ(request):
    return render(request, 'templ.html', {"new_dict":new_dict})


def todo(request):

    return render(request,"todo.html",{"new_dict":new_dict})


def add(request):
    print("Добавляем задачу в БД")
    return HttpResponse()



