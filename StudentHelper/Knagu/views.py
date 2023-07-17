from django.shortcuts import render
# Create your views here.
from .forms import Autorization
from RETURN_SUB import *
from titulnikKnagu  import *
from GetDir import *
import os


def index_page(request):
    if request.method == 'POST':
        form = Autorization(request.POST)
    else:
        form = Autorization()
    return render(request, "index.html", {'form': form})

i = 0
def get_data(request):
    global i
    if i == 0:
        form = Autorization(request.POST)
        login = form['login'].value()
        password = form['password'].value()
        out_info = parseLK(username=login, password=password, course=1)
        for item in out_info["marks"]:
            sub = item.split("_")
            if not(sub[1] == "Зачет" or sub[1] == "Экзамен" or sub[1] == "Итоговая оценка"):
                edit_template(sub=sub[0],type_sub=sub[1])


    all_subjects_name = GetDir()
    new_dict = {}
    for key, value_list in all_subjects_name.items():
        new_dict[key] = value_list
    i = 1
    return render(request, 'main.html', {"new_dict":new_dict})


def gen(request):
    return render (request,"gen.html")