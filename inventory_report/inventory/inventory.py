import csv
import json
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory:
    @classmethod
    def read(cls, path: str):

        if path.endswith('.csv'):
            with open(path) as data:
                reader = csv.DictReader(data)
                data = list(reader)
                return data

        if path.endswith('.json'):
            with open(path) as data:
                return json.load(data)

        elif path.endswith('.xml'):

            return XmlImporter.import_data(path)

    @classmethod
    def import_data(cls, path, type):
        final_result = Inventory.read(path)
        if type == "simples":
            return SimpleReport.generate(final_result)
        elif type == "completo":
            return CompleteReport.generate(final_result)
        else:
            raise ValueError("Tipo de relatório inválido")
