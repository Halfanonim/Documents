import re

def convert_filenames(event_info, filenames):
    # Словарь для хранения событий и их файлов
    events = {}
    
    # Проходим по информации о событиях и заполняем словарь events
    for line in event_info:
        parts = line.split()
        event_name = '_'.join(parts[:-3]).upper()  # Преобразуем название события к верхнему регистру
        year = parts[-3]
        month = parts[-2]
        day = parts[-1]
        events[(year, month, day)] = event_name
    
    # Словарь для хранения порядковых номеров файлов событий
    event_counters = {event_name: 1 for event_name in events.values()}
    
    # Список для хранения преобразованных имен файлов
    converted_filenames = []
    
    # Проходим по всем именам файлов
    for filename in filenames:
        # Находим соответствие с помощью регулярного выражения
        match = re.match(r'^(IMG|DCIM)-?(\d{4})(\d{2})(\d{2})(\d+)\.jpg$', filename)
        if match:
            groups = match.groups()
            prefix = groups[0]  # Префикс IMG или DCIM
            year = groups[1]
            month = groups[2]
            day = groups[3]
            serial_number = int(groups[4])
            
            # Находим соответствующее событие по дате
            event_name = events.get((year, month, day))
            
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
            new_filename = f"{year}_{month_text}_{day}_{event_name}_{event_counters[event_name]}.jpg"
            
            # Увеличиваем счетчик для текущего события
            event_counters[event_name] += 1
            
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
    result = convert_filenames(event_info, filenames)
    
    # Вывод результата
    for filename in result:
        print(filename)
