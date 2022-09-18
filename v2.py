def repeat():
    repeat_inn = input('Хотите добавить новый отдел (введите "y" или "n"): ')
    while True:
        if repeat_inn == 'y':
            def name_department():
                with open('personnel.txt', 'a') as department:
                    dep = department.write(input('Ведите название отдела:'))
                    return dep

            def number_of_staff_department():
                with open('personnel.txt', 'a') as number_of_staff:
                    nos = number_of_staff.write(number_of_staff_add)
                return nos

            def add_worker():
                with open('personnel.txt', 'a') as add_worker_in:
                    dict = {}
                    for age_spec in range(1, number_of_staff_add + 1):
                        name = input('Введите имя сотрудника: ')
                        age_spec = {input('Введите возраст сотрудника: '), input('Введите специальность сотрудника: ')}
                        dict[name] = age_spec
                        add_sp = add_worker_in.writelines(f'{dict}\n')
                return add_sp

            name_department()
            number_of_staff_add = input('Ведите колличество работников: ')
            number_of_staff_department()
            number_of_staff_add = int(number_of_staff_add)
            add_worker()
            repeat()

        elif repeat_inn == 'n': print('Работа окончена')
        break
repeat()