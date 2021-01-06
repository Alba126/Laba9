#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Вариант 18. Использовать словарь, содержащий следующие ключи: название товара; название
# магазина, в котором продается товар; стоимость товара в руб. Написать программу,
# выполняющую следующие действия: ввод с клавиатуры данных в список, состоящий из
# словарей заданной структуры; записи должны быть размещены в алфавитном порядке по
# названиям магазинов; вывод на экран информации о товарах, продающихся в магазине,
# название которого введено с клавиатуры; если такого магазина нет, выдать на дисплей
# соответствующее сообщение.

# Для варианта задания лабораторной работы 8 необходимо дополнительно
# реализовать сохранение и чтение данных из файла формата JSON. Необходимо проследить за
# тем, чтобы файлы генерируемый этой программой не попадали в репозиторий лабораторной
# работы.


import sys
import json
import xml.etree.ElementTree as ET

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

            # Вывести данные о всех товарах.
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
            sel = (parts[1])

            count = 0
            for markets in market:
                if markets.get('shop') == sel:

                    count += 1
                    print(
                        '{:>4}: {}'.format(count, markets.get('shop', ''))
                    )
                    print('Название товара:', markets.get('product', ''))
                    print('Стоимость в руб.:', markets.get('price', ''))

            # Если счетчик равен 0, то продукты не найдены.
            if count == 0:
                print("Продукт не найден.")

        elif command.startswith('load '):
            parts = command.split(' ', maxsplit=1)

            if 'xml' in parts[1]:
                print('Загрузка')
            elif 'json' in parts[1]:
                with open(parts[1], 'r') as f:
                    markets = json.load(f)

        elif command.startswith('save '):
            parts = command.split(' ', maxsplit=1)

            if 'xml' in parts[1]:
                print('Сохранение')
            elif 'json' in parts[1]:
                with open(parts[1], 'w')as f:
                    json.dump(markets, f)

        elif command == 'help':
            # Вывести справку о работе с программой.
            print("Список команд:\n")
            print("add - добавить продукт;")
            print("list - вывести список продуктов;")
            print("select <товар> - информация о товаре;")
            print("load <имя файла> - загрузить данные из файла;")
            print("save <имя файла> - сохранить данные в файл;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")

        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)
            