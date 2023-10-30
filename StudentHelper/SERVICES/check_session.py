from datetime import datetime

def session_calculation(target_date_str:str):
    # Получаем текущую дату
    current_date = datetime.now()

    # Преобразуем строку целевой даты в объект datetime
    target_date = datetime.strptime(target_date_str, "%d.%m.%Y")

    # Рассчитываем разницу в днях между текущей и целевой датой
    days_diff = (target_date - current_date).days

    return days_diff


print(session_calculation("10.01.2024"))
