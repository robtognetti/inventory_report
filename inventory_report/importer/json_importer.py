import json

from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, path):
        if path.endswith('.json'):

            with open(path, encoding="utf8") as file:
                reader = json.load(file)
                return reader
        else:
            raise ValueError("Arquivo inválido")
