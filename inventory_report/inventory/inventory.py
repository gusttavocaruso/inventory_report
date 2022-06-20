from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter


class Inventory():
    def import_data(path, report_type):

        if path.endswith('.csv'):
            file = CsvImporter.import_data(path)
        elif path.endswith('.json'):
            file = JsonImporter.import_data(path)
        elif path.endswith('.xml'):
            file = XmlImporter.import_data(path)

        if report_type == 'simples':
            return SimpleReport.generate(file)

        return CompleteReport.generate(file)
