file_data_txt = open('data.txt', encoding='utf8')# открытие файла

read_data_txt = file_data_txt.read() #чтение файла
# print(read_data_txt)

file_data_txt.close() #закрытие файла

# ускоряем работу с файлами припомощи контентного менеджера with
with open('data.txt', encoding='utf8') as file_data_txt: #with после прочтения файла сам его закрывает
    read_data_txt = file_data_txt.read()
    # print(read_data_txt)


# методы чтения файла
with open('data.txt', encoding='utf8') as file_data_txt: #read считывает весь файл целиком (class str)
    read_data_txt = file_data_txt.read()
    print(read_data_txt)

with open('data.txt', 'r', encoding='utf8') as file_data_txt: #'r' явно указываем режим чтения
    read_data_txt = file_data_txt.readline() #readline считывет за раз только одну строку (class str)
    print(read_data_txt)

with open('data.txt', encoding='utf8') as file_data_txt:
    read_data_txt = file_data_txt.readlines() #readlines считывет весь файл, но посторочно помещаяя каждую строку в список (class list)
    print(read_data_txt)