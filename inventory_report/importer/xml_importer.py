import xmltodict
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    def import_data(path):
        if path.endswith('.xml'):
            with open(path) as file:
                xml_to_dict = xmltodict.parse(file.read(), 'UTF-8')
                response = xml_to_dict['dataset']['record']
                return response
        else:
            raise ValueError('Arquivo inválido')
