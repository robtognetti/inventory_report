from inventory_report.reports.simple_report import SimpleReport


# mentoria maria carolina Weather Report
class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, list):
        simple_report = SimpleReport.generate(list)
        produ_enterprise = {}
        for product in list:
            if product['nome_da_empresa'] not in produ_enterprise:
                produ_enterprise[product['nome_da_empresa']] = 1
            else:
                produ_enterprise[product['nome_da_empresa']] += 1
        format = "Produtos estocados por empresa:\n"
        for enterprise in produ_enterprise:
            format += f"- {enterprise}: {produ_enterprise[enterprise]}\n"
        return (
            f"{simple_report}\n"f"{format}"
        )
