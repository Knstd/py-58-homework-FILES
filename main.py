from pprint import pprint
import os

file_name = 'recipes.txt'


def cooking_book(file_name):
    cook_book = {}
    with open(file_name, encoding='utf-8') as file:
        for line in file:
            dish = line.strip()
            ingridients = []
            for i in range(int(file.readline())):
                ingridient = file.readline().strip().split(' | ')
                column_names = ['ingridient_name', 'quantity', 'measure']
                dish_ingridients = dict(zip(column_names, ingridient))
                ingridients.append(dish_ingridients)
            file.readline()
            cook_book[dish] = ingridients
    return cook_book


# pprint(cooking_book(file_name), width=120, sort_dicts=False)
# print()


def get_shop_list_by_dishes(dishes, person_count):
    dishes_dict = cooking_book(file_name)
    ingridient_list = {}
    for dish in dishes:
        if dish in dishes_dict:
            for ingridient in dishes_dict[dish]:
                if ingridient['ingridient_name'] in ingridient_list:
                    ingridient_list[ingridient['ingridient_name']]['quanity'] += int(ingridient['quantity']) * person_count
                else:
                    ingridient_list[ingridient['ingridient_name']] = {'measure': ingridient['measure'], 'quanity': int(ingridient['quantity']) * person_count}
        else:
            return f'Такого блюда нет - {dish}'
    return ingridient_list

# pprint(get_shop_list_by_dishes(['Омлет', 'Омлет', 'Фахитос'], 8))

FILES_CATALOG_NAME = 'files'
FILE_1_NAME = '1.txt'
FILE_2_NAME = '2.txt'
FILE_3_NAME = '3.txt'
RESULT = 'result.txt'
BASE_PATH = os.getcwd()

file_1_path = os.path.join(BASE_PATH, FILES_CATALOG_NAME, FILE_1_NAME)
file_2_path = os.path.join(BASE_PATH, FILES_CATALOG_NAME, FILE_2_NAME)
file_3_path = os.path.join(BASE_PATH, FILES_CATALOG_NAME, FILE_3_NAME)
result_path = os.path.join(BASE_PATH, FILES_CATALOG_NAME, RESULT)

def file_lenght(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        lenght = 0
        for i in f:
            lenght += 1
        return lenght

def sort_files(file_1, file_2, file_3, result):
    with open(file_1_path, 'r', encoding='utf-8') as file_1,\
         open(file_2_path, 'r', encoding='utf-8') as file_2,\
         open(file_3_path, 'r', encoding='utf-8') as file_3,\
         open(result_path, 'a', encoding='utf-8') as result:
            file_list = {FILE_1_NAME: [file_1.read(), (file_lenght(file_1_path))],\
                         FILE_2_NAME: [file_2.read(), (file_lenght(file_2_path))],\
                         FILE_3_NAME: [file_3.read(), (file_lenght(file_3_path))]}
            file_list_sorted = sorted(file_list.items(), key=lambda v: v[1][1])
            for file in file_list_sorted:
                result.write(f'{file[0]}\n')
                result.write(f'{str(file[1][1])}\n')
                result.write(f'{file[1][0]}\n')


sort_files(file_1_path, file_2_path, file_3_path, result_path)


