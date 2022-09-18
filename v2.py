def repeat():
    repeat_inn = input('Хотите добавить новый отдел (введите "y" или "n"): ')
    while True:
        if repeat_inn == 'y':
            def name_department():
                with open('personnel.txt', 'a') as department:
                    dep = department.write(f'Название отдела: {input("Ведите название отдела: ")}\n')
                    return dep

            def number_of_staff_department():
                with open('personnel.txt', 'a') as number_of_staff:
                    nos = number_of_staff.write(f'Колличество сотрудников: {number_of_staff_add}\n')
                return nos

            def add_worker():
                with open('personnel.txt', 'a') as add_worker_in:
                    for age_spec in range(1, number_of_staff_add + 1):
                        name = f'{input("Введите имя сотрудника: ")}\n'
                        age_worker = f'Возраст: {input("Введите возраст сотрудника: ")} лет,'
                        spec_worker = f'Специальность: {input("Введите специальность сотрудника: ")}'
                        add_sp = add_worker_in.writelines(f'{name}{age_worker} | {spec_worker}\n')
                    return add_sp

            name_department()
            number_of_staff_add = input('Ведите колличество сотрудников: ')
            
            number_of_staff_department()
            number_of_staff_add = int(number_of_staff_add)
            add_worker()
            repeat()

        elif repeat_inn == 'n': print('Работа окончена')
        break
repeat()