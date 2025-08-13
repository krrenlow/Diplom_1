class Data:

    param = 'bun_name, bun_price, ingredient_type, ingredient_name, ingredient_price, expected_burger_price'
    value = [
        ['Булочка', 500, 'SAUSE', 'Острый', 50, 1050],
        ['super_bun', 200, 'FILLING', 'перец', 70, 470],
        ['1+1', 100, 'SAUSE', '', 0, 200],
        ['Лучший вариант', 300.57, '', '', 0, 601.14],
        ['The best', 592.15, 'FILLING', 'bam', 100.01, 1284.31]
    ]

    NAME_BUN = 'Тестовая'
    PRICE_BUN = 300
    NAME_INGREDIENT_1 = 'пикантный'
    PRICE_INGREDIENT_1 = 90
    NAME_INGREDIENT_2 = 'сырный'
    PRICE_INGREDIENT_2 = 50
    NAME_INGREDIENT_3 = 'грибы'
    PRICE_INGREDIENT_3 = 150
    RECEIPT = (f'(==== {NAME_BUN} ====)\n'
               f'= sauce {NAME_INGREDIENT_1} =\n'
               f'= filling {NAME_INGREDIENT_3} =\n'
               f'(==== {NAME_BUN} ====)\n'
               '\n'
               'Price: 840')