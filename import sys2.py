import re

def convert_filename(file_name):
    # Шаблоны для различных форматов
    patterns = [
        r'^IMG_(\d{4})(\d{2})(\d{2})_(\d{2})(\d{2})(\d{2})(\d+)\.jpg$',  # IMG_20230430_092422111.jpg
        r'^DCIM-(\d{4})-(\d{2})-(\d{2})-(\d+)\.jpg$',                      # DCIM-2023-04-30-1.jpg
        r'^(\d{4})(\d{2})(\d{2})(\d{2})(\d{2})(\d{2})-(\d+)\.jpg$'        # 202304300924-1.jpg
    ]
    
    # Месяцы в текстовом формате
    months_dict = {
        '01': 'Jan', '02': 'Feb', '03': 'Mar', '04': 'Apr', 
        '05': 'May', '06': 'Jun', '07': 'Jul', '08': 'Aug', 
        '09': 'Sep', '10': 'Oct', '11': 'Nov', '12': 'Dec'
    }
    
    # Поиск подходящего шаблона
    for pattern in patterns:
        match = re.match(pattern, file_name)
        if match:
            groups = match.groups()
            if pattern == patterns[0]:  # IMG format
                year, month, day, hour, minute, second, microsec = groups
            elif pattern == patterns[1]:  # DCIM format
                year, month, day, _ = groups
                hour, minute, second, microsec = '00', '00', '00', '000'
            elif pattern == patterns[2]:  # Generic format
                year, month, day, hour, minute, second, microsec, _ = groups
            
            # Преобразуем числовой месяц в текстовый формат
            month_text = months_dict[month]
            
            # Формируем новое имя файла
            new_file_name = f"{year}_{month_text}_{day}_PYTHON_CONFERENCE.jpg"
            
            return new_file_name
    
    return None

# Чтение данных из stdin
if __name__ == "__main__":
    import sys
    input_data = sys.stdin.read().strip()
    
    # Конвертация имени файла
    converted_name = convert_filename(input_data)
    
    # Вывод результата
    if converted_name:
        print(converted_name)
