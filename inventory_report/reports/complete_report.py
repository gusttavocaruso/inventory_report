# import json
from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    def generate(product_list):
        # with open(path) as file:
        # product_list = json.load(file)

        estoque_empresa = []

        for product in product_list:
            estoque_empresa.append(product["nome_da_empresa"])

        companies_list = []
        for name in estoque_empresa:
            count_companies = estoque_empresa.count(name)
            companies_list.append(dict(name=name, count=count_companies))

        test_string = ""
        estoque_por_empresa = Counter(estoque_empresa)
        for key, value in estoque_por_empresa.items():
            test_string += f'- {key}: {value}\n'
        simple_report = SimpleReport.generate(product_list)

        return (
            f'{simple_report}\n'
            f'Produtos estocados por empresa: \n'
            f'{test_string}'
        )

# Requisito desenvolvido em pair programming!
