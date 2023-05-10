from abc import ABC


class Importer(ABC):
    @staticmethod
    def import_data(cls, path):
        raise NotImplementedError
