import xml.etree.ElementTree as Et

from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, path: str):
        especific = path.split('.')[-1]
        if especific != 'xml':
            raise ValueError("Arquivo inválido")

        tree = Et.parse(path)

        data = []

        root = tree.getroot()
        for elements in root:
            item = {}
            for subelemen in elements:
                item[subelemen.tag] = subelemen.text
            data.append(item)
        return data
