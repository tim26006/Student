import docx

import os


def edit_template(sub:str,type_sub:str, group:str)->None:
    if type_sub=='Контрольная':
        type_sub = "КОНТРОЛЬНАЯ РАБОТА"
    if type_sub=='РГР':
        type_sub = "РАСЧЁТНО-ГРАФИЧЕСКАЯ РАБОТА"
    replace_dict = {
        "РАБОТА": type_sub,
        "по дисциплине «Математический анализ»":f"по дисциплине «{sub}»",
        "2ИТБ-2": group
    }

    doc = docx.Document("./Knagu/static/subject_templates/sample.docx")


    style = doc.styles['Normal']
    font = style.font
    font.name = 'Times New Roman'
    font.size = docx.shared.Pt(14)

    for replace_elem in replace_dict:
        for p in doc.paragraphs:
            if p.text.find(replace_elem) >=0:
                p.text = p.text.replace(replace_elem,replace_dict[replace_elem])
    file = f"{sub}*{type_sub}*.docx"
    doc.save("./Knagu/static/subject_templates/"+file)