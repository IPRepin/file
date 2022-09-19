# def repeat():
#     repeat_inn = input('Хотите добавить новый отдел (введите "y" или "n"): ')
#     while True:
#         if repeat_inn == 'y':
#             def name_department():
#                 with open('personnel.txt', 'a') as department:
#                     dep = department.write(f'Название отдела: {input("Ведите название отдела: ")}\n')
#                     return dep
#
#             def number_of_staff_department():
#                 with open('personnel.txt', 'a') as number_of_staff:
#                     nos = number_of_staff.write(f'{number_of_staff_add}\n')
#                 return nos
#
#             def add_worker():
#                 with open('personnel.txt', 'a') as add_worker_in:
#                     for age_spec in range(1, number_of_staff_add + 1):
#                         name = f'{input("Введите имя сотрудника: ")}\n'
#                         age_worker = f'Возраст: {input("Введите возраст сотрудника: ")} лет'
#                         spec_worker = f'Специальность: {input("Введите специальность сотрудника: ")}'
#                         add_sp = add_worker_in.writelines(f'{name}{age_worker} | {spec_worker}\n')
#                     return add_sp
#
#             name_department()
#             number_of_staff_add = input('Ведите колличество сотрудников: ')
#
#             number_of_staff_department()
#             number_of_staff_add = int(number_of_staff_add)
#             add_worker()
#             repeat()
#
#         elif repeat_inn == 'n': print('Работа окончена')
#         break
#
# repeat()

def read_personel_txt():
    depatments = []
    with open('personnel.txt', 'rt') as emloyees_list:
        for line in emloyees_list:
            depatment_name = line
            depatment = {"name": depatment_name, "employees": []}
            emloyees_count = emloyees_list.readline()
            for i in range(int(emloyees_count)):
                name = emloyees_list.readline()
                emp = emloyees_list.readline()
                age_pers, position = emp.split(' | ')
                emloyee = {"name": name, "age": age_pers, "position": position}
                depatment["employees"].append(emloyee)
            depatments.append(depatment)
    print(depatments)

read_personel_txt()
