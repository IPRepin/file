file_data_txt = open('data.txt', encoding='utf8')# открытие файла

read_data_txt = file_data_txt.read() #чтение файла
# print(read_data_txt)

file_data_txt.close() #закрытие файла

# ускоряем работу с файлами при помощи контентного менеджера with
with open('data.txt', encoding='utf8') as file_data_txt: #with после прочтения файла сам его закрывает
    read_data_txt = file_data_txt.read()
    # print(read_data_txt)


# методы чтения файла
with open('data.txt', encoding='utf8') as file_data_txt: #read считывает весь файл целиком (class str)
    read_data_txt = file_data_txt.read()
    # print(read_data_txt)
    # print()

with open('data.txt', 'r', encoding='utf8') as file_data_txt: #'r' явно указываем режим чтения
    read_data_txt = file_data_txt.readline() #readline считывет за раз только одну строку (class str)
    # print(read_data_txt)

with open('data.txt', encoding='utf8') as file_data_txt:
    read_data_txt = file_data_txt.readlines() #readlines считывет весь файл, но посторочно помещаяя каждую строку в список (class list)
    # print(read_data_txt)

# with open('data.txt', 'r', encoding='utf8') as file_data_txt:
#     for line in file_data_txt:
        # print(line)


#методы запист в файл

# writh - записывает по одной строке


with open('data_recording.txt', 'w') as file_record: # 'w' - перезапись файла.
    record_1 = file_record.write('Hello world!\n')
    record_2 = file_record.write('Привет мир!\n')

with open('data_recording.txt', 'a') as file_record: #'a' - дозапись файла
    record_3 = file_record.write('Дозаписанная строка\n')

# writhlines - записывает список(картеж, словарь) из нескольких строк
with open('data_recording.txt', 'a') as file_writlines:
    dict1 = {'Name': input('Введите ваше имя: '), 'Age': input('Введите ваш возраст: ')}
    for key, value in dict1.items():
        lst = file_writlines.writelines(f'{key}: {value}\n')

with open('data_recording.txt', 'a') as file_writlines:
    dict1 = {'Work': input('Введите профессию: '), 'Cours': input('Введите образование: ')}
    for key, value in dict1.items():
        file_writlines.seek(0) # переводит курсор к выбранному символу по его индексу
        lst = file_writlines.writelines(f'{key}: {value}\n')
