import os


def get_shop_list_by_dishes(dishes, person_count, cook_book):
    shop_list = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            new_shop_list_item = dict(ingredient)
            new_shop_list_item['quantity'] *= person_count
            if new_shop_list_item['ingridient_name'] not in shop_list:
                shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item
            else:
                shop_list[new_shop_list_item['ingridient_name']]['quantity'] += new_shop_list_item['quantity']
    return shop_list


def print_shop_list(shop_list):
    for shop_list_item in shop_list.values():
        print('{} {} {}'.format(shop_list_item['ingridient_name'], shop_list_item['quantity'], shop_list_item['measure']))


def create_shop_list():
    dishes = input('Введите блюда в расчете на одного человека (через запятую): ') \
        .lower().split(', ')
    return dishes


def get_ingredients_from_string(receipt):
    dict_ingredients = {}
    list_ingredients = receipt[2:]
    list_local = []
    for i in range(int(receipt[1])):
        ingridients = list_ingredients[i].split(' | ')
        list_local.append({'ingridient_name': ingridients[0].lower(),
                     'quantity': int(ingridients[1].lower()),
                     'measure': ingridients[2].lower()})
    dict_ingredients[receipt[0].lower()] = list_local
    return dict_ingredients


def get_from_file():
    cook_book = {}
    script_dir = os.path.dirname(__file__)
    ingredients = []
    with open(os.path.join(script_dir, 'reciept.txt'), 'r') as receipts_from_file:
        for line in receipts_from_file:
            line = line.strip('\n')
            if line:
                ingredients.append(line)
            else:
                cook_book.update(get_ingredients_from_string(ingredients))
                ingredients.clear()
    person_count = int(input('Введите количество человек: '))
    dishes = create_shop_list()
    shop_list = get_shop_list_by_dishes(dishes, person_count, cook_book)
    print_shop_list(shop_list)


get_from_file()
