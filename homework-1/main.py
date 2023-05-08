"""Скрипт для заполнения данными таблиц в БД Postgres."""
import csv
import os


class InstantiateCSVError:
    pass


def instantiate_from_csv(file_mame):
    """Открытие файла csv"""
    all = []
    if not os.path.exists(file_mame):
        raise FileNotFoundError('Отсутствует файл item.csv')

    with open(os.path.join(file_mame), 'r') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            if len(row) != 3:
                raise InstantiateCSVError("Файл item.csv поврежден")
            name = row[0]
            price = int(row[1])
            quantity = int(row[2])
            cls(name, price, quantity)
