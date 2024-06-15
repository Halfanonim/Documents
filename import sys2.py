import sys

def rename_file(file_name):
    # Разбиваем имя файла по разделителям для извлечения компонентов
    parts = file_name.split('_')
    
    # Получаем год, месяц, день, час, минуту и микросекунды из имени файла
    year = parts[1][:4]
    month = parts[1][4:6]
    day = parts[1][6:8]
    
    # Преобразуем числовой месяц в текстовый формат
    months_dict = {
        '01': 'Jan', '02': 'Feb', '03': 'Mar', '04': 'Apr', 
        '05': 'May', '06': 'Jun', '07': 'Jul', '08': 'Aug', 
        '09': 'Sep', '10': 'Oct', '11': 'Nov', '12': 'Dec'
    }
    month_text = months_dict[month]
    
    # Собираем новое имя файла с учетом названия события и расширения
    new_file_name = f"{year}_{month_text}_{day}_PYTHON_CONFERENCE.jpg"
    
    return new_file_name

# Чтение данных из stdin
if __name__ == "__main__":
    input_data = sys.stdin.read().strip().splitlines()
    
    for line in input_data:
        new_name = rename_file(line.strip())
        print(new_name)
