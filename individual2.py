# -*- coding: utf-8 -*-

# Вариант 18. Использовать словарь, содержащий следующие ключи: название товара; название
# магазина, в котором продается товар; стоимость товара в руб. Написать программу,
# выполняющую следующие действия: ввод с клавиатуры данных в список, состоящий из
# словарей заданной структуры; записи должны быть размещены в алфавитном порядке по
# названиям магазинов; вывод на экран информации о товарах, продающихся в магазине,
# название которого введено с клавиатуры; если такого магазина нет, выдать на дисплей
# соответствующее сообщение.

import sys
import json

if __name__ == '__main__':
    # Список .
    market = []

    # Организовать бесконечный цикл запроса команд.
    while True:
        # Запросить команду из терминала.
        command = input(">>> ").lower()

        # Выполнить действие в соответствие с командой.
        if command == 'exit':
            break

        elif command == 'add':
            # Запросить данные .
            shop = input("Название магазина? ")
            product = input("Название товара? ")
            price = float(input("Стоимость товара в руб.? "))

            # Создать словарь.
            markets = {
                'shop': shop,
                'product': product,
                'price': price,
            }

            # Добавить словарь в список.
            market.append(markets)
            # Отсортировать список в случае необходимости.
            if len(market) > 1:
                market.sort(key=lambda item: item.get('shop', ''))

        elif command == 'list':
            # Заголовок таблицы.
            line = '+-{}-+-{}-+-{}-+-{}-+'.format(
                '-' * 4,
                '-' * 30,
                '-' * 20,
                '-' * 20
            )
            print(line)
            print(
                '| {:^4} | {:^30} | {:^20} | {:^20} |'.format(
                    "No",
                    "Магазин",
                    "Товар",
                    "Стоимость в руб."
                )
            )
            print(line)

            # Вывести данные о всех магазинах и товарах в них.
            for idx, markets in enumerate(market, 1):
                print(
                    '| {:>4} | {:<30} | {:<20} | {:>20} |'.format(
                        idx,
                        markets.get('shop', ''),
                        markets.get('product', ''),
                        markets.get('price', 0)
                    )
                )

            print(line)

        elif command.startswith('select '):
            parts = command.split(' ', maxsplit=2)
            period = str(parts[1])
            count = 0

            for markets in market:
                if markets.get('shop') == period:
                    count += 1
                    print(
                        '{:>4}: {}'.format(count, markets.get('shop', ''))
                    )
                    print('Название товара:', markets.get('product', ''))
                    print('Стоимость в руб.:', markets.get('price', ''))

            # Если счетчик равен 0, то магазины не найдены.
            if count == 0:
                print("Такого магазина нет!")

        elif command.startswith('load '):
            # Разбить команду на части для выделения имени файла.
            parts = command.split(' ', maxsplit=1)
            # Прочитать данные из файла JSON.
            with open(parts[1], 'r') as f:
                market = json.load(f)

        elif command.startswith('save '):
            # Разбить команду на части для выделения имени файла.
            parts = command.split(' ', maxsplit=1)
            # Сохранить данные в файл JSON.
            with open(parts[1], 'w') as f:
                json.dump(market, f)

        elif command == 'help':
            # Вывести справку о работе с программой.
            print("Список команд:\n")
            print("add - добавить продукт;")
            print("list - вывести список продуктов;")
            print("select <товар> - информация о товаре;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")

        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)
