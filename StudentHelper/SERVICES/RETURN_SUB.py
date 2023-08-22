from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
def parseLK(username: str, password: str, course: int) -> dict:
    """ Данный веб-сервис берёт информацию с личного кабинета студента"""

    return_dict = {}
    webdriver_service = Service('./chromedriver.exe')

    driver = webdriver.Chrome(service=webdriver_service)

    driver.get("https://student.knastu.ru/")
    driver.find_element_by_css_selector("input[type=text]").send_keys(username)
    driver.find_element_by_css_selector("input[type=password]").send_keys(password)

    driver.find_element_by_css_selector("button[type=submit]").click()
    time.sleep(5)
    # if course==1:
    #     driver.find_elements_by_xpath(".//button[@class='select_course__btn btn btn-primary']")[0].click()
    # if course==2:
    #     driver.find_elements_by_xpath(".//button[@class='select_course__btn btn btn-outline-primary']")[0].click()
    # if course == 3:
    #     driver.find_elements_by_xpath(".//button[@class='select_course__btn btn btn-outline-primary']")[1].click()
    # if course == 4:
    #     driver.find_elements_by_xpath(".//button[@class='select_course__btn btn btn-outline-primary']")[2].click()

    # time.sleep(5)

    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    all_subjects = soup.findAll('div', class_='row gx-0')
    text2marks = {
    "отлично":5,
    "хорошо": 4,
    "удовлевтворительно:":3,
    "зачтено":5,
    "не зачтено":2,
    "-": "-"
}
    marks = {}
    for x, subject in enumerate(all_subjects,start=1):

        try:
            work_type = subject.find("span",class_="ps-2").text
            sub = subject.find("a",class_="rpd_link_in_yp").text
            mark = subject.find("div", class_="col-6 col-md-3 col-lg px-1 d-flex align-items-center").find("span",class_="ps-2").text.strip()

            marks[f'{sub}_{work_type}']=text2marks[mark]

        except: continue
    name_student = (soup.find("h6" , class_='mt-1').text).split(" ")
    name_student = f"{name_student[0]} {name_student[1]}"
    group = (soup.find("h5" , class_='ms-2 my-auto').text).split(" ")
    return_dict["marks"] = marks
    return_dict["student"] = name_student
    return_dict["group"] = group[1]
    return return_dict


#templ = parseLK("Sidorin.TS",'79303418',1)
