def read_cook_book():
    with open('recipes.txt', 'rt', encoding='utf8') as reading_cook_book:
        for line in reading_cook_book:
            name_of_the_dish = line.strip()
            ingredients_count = reading_cook_book.readline()
            dishs = []
            for i in range(int(ingredients_count)):
                ingredient = reading_cook_book.readline()
                ingredient_name, quantity, measure = ingredient.split(' | ')
                ingredient_dict = {"ingredient_name": ingredient_name, "quantity": quantity, "measure": measure}
                dishs.append(ingredient_dict)

            cook_book[name_of_the_dish] = dishs
            reading_cook_book.readline()
        print(cook_book)

cook_book = {}
read_cook_book()

# def get_shop_list_by_dishes(dishes, person_count):
#     person_count = int(input('Ведите количество персон'))
#     for dishes in getcook_book:
