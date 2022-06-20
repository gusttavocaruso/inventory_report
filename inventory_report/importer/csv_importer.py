import csv
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    def import_data(path):
        if path.endswith('.csv'):
            with open(path) as file:
                return list(csv.DictReader(file))
        else:
            raise ValueError('Arquivo inválido')


# Checar extensão:
# https://www.adamsmith.haus/python/answers/how-to-check-the-extension-of-a-file-in-python
