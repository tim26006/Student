import openai
from StudentHelper import settings

openai.api_key = settings.GPT_TOKEN

def GPTResponse(theme:str, amount:int) -> dict:
  prompt = f" источники литературы по теме: {theme}. Выводи списком, с указанием автора и кол-ва страниц. Выводи в таком формате: Виленкин, С. Я. Математическое обеспечение управляющих вычислительных машин / С. Я. Виленкин, Э. А. Трахтенгерц. - М. : Энергия, 1972. - 392 с. В конце каждого источника ставь ; Количество источников: {amount}. все источники выводи на русском языке."
  dictOfSourses = {}

  response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=prompt,
    max_tokens=1500
  )
  listOfSourses = (response.choices[0].text).split(";")
  for x,i in enumerate(listOfSourses):
      dictOfSourses[x] = i.strip()

  return dictOfSourses

print (GPTResponse(theme = "Notion", amount = 10))