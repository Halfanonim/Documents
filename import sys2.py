import re

def convert_filename(event_info, filenames):
    # Разбиваем информацию о событиях на список кортежей (event_name, year, month, day)
    events = [line.split() for line in event_info]
    
    # Список для хранения преобразованных имен файлов
    converted_filenames = []
    
    # Счетчик для нумерации файлов с одного события
    event_counters = {}
    
    # Проходим по всем именам файлов
    for filename in filenames:
        # Находим соответствие с помощью регулярного выражения
        match = re.match(r'^(IMG|DCIM)-?(\d{4})-(\d{2})-(\d{2})-(\d+).jpg$', filename)
        if match:
            groups = match.groups()
            prefix = groups[0]  # Префикс IMG или DCIM
            year = groups[1]
            month = groups[2]
            day = groups[3]
            serial_number = int(groups[4])
            
            # Находим соответствующее событие по дате
            event_name = None
            for event in events:
                if event[1] == year and event[2] == month and event[3] == day:
                    event_name = event[0]
                    break
            
            if event_name is None:
                continue
            
            # Преобразуем числовой месяц в текстовый формат
            months_dict = {
                '01': 'Jan', '02': 'Feb', '03': 'Mar', '04': 'Apr', 
                '05': 'May', '06': 'Jun', '07': 'Jul', '08': 'Aug', 
                '09': 'Sep', '10': 'Oct', '11': 'Nov', '12': 'Dec'
            }
            month_text = months_dict[month]
            
            # Объединяем название события, дату и порядковый номер
            if event_name not in event_counters:
                event_counters[event_name] = 1
            else:
                event_counters[event_name] += 1
            
            new_filename = f"{year}_{month_text}_{day}_{event_name}_{event_counters[event_name]}.jpg"
            
            # Добавляем преобразованное имя файла в список
            converted_filenames.append(new_filename)
    
    # Сортируем список преобразованных имен файлов по алфавиту
    converted_filenames.sort()
    
    # Возвращаем отсортированный список преобразованных имен файлов
    return converted_filenames

# Чтение данных из stdin
if __name__ == "__main__":
    import sys
    input_data = sys.stdin.read().strip().split('\n')
    
    # Разделяем данные на информацию о событиях и имена файлов
    event_info = input_data[:3]
    filenames = input_data[3:]
    
    # Конвертация и сортировка имен файлов
    result = convert_filename(event_info, filenames)
    
    # Вывод результата
    for filename in result:
        print(filename)
