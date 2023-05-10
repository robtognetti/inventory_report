from datetime import datetime
from collections import Counter


# mentoria maria carolina weather report
class SimpleReport:
    @classmethod
    def generate(cls, list):
        company = [item["nome_da_empresa"] for item in list]
        company_most_common = Counter(company).most_common(1)[0][0]
        date_expirate = min(
            (
                item['data_de_validade']
                for item in list
                if item['data_de_validade'] is not None
                and datetime.now().strftime("%Y-%m-%d")
                <= item['data_de_validade']
            )
        )
        old = min([product["data_de_fabricacao"] for product in list])
        return (
            f"Data de fabricação mais antiga: {(old)}\n"
            f"Data de validade mais próxima: {(date_expirate)}\n"
            f"Empresa com mais produtos: {company_most_common}"
        )
