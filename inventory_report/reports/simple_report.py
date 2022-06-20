# import json
from datetime import datetime
from collections import Counter


class SimpleReport:
    def generate(product_list):
        # with open(path) as file:
        # product_list = json.load(file)

        datas_fabricacao = []
        datas_validade = []
        estoque_empresa = []
        hoje = datetime.today().strftime('%Y-%m-%d')

        for product in product_list:
            datas_fabricacao.append(product["data_de_fabricacao"])

            if product["data_de_validade"] >= hoje:
                datas_validade.append(product["data_de_validade"])

            estoque_empresa.append(product["nome_da_empresa"])

        validade_mais_proxima = min(datas_validade)
        fabricacao_mais_antiga = min(datas_fabricacao)
        estoque_por_empresa = Counter(estoque_empresa)
        maior_estoque = estoque_por_empresa.most_common()[0][0]

        return (
          f'Data de fabricação mais antiga: {fabricacao_mais_antiga}\n'
          f'Data de validade mais próxima: {validade_mais_proxima}\n'
          f'Empresa com maior quantidade de produtos '
          f'estocados: {maior_estoque}\n'
        )

# Requisito desenvolvido em pair programming!
