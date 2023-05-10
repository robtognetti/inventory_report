from inventory_report.inventory.product import Product


def test_relatorio_produto():
    product = Product(
        id=1,
        nome_do_produto="Produto any",
        nome_da_empresa="Empresa any",
        data_de_fabricacao="2027-09-11",
        data_de_validade="2029-04-09",
        numero_de_serie="j4b1l3u",
        instrucoes_de_armazenamento="seco e fresco"
    )

    assert product.__repr__() == (
        f"O produto {product.nome_do_produto}"
        f" fabricado em {product.data_de_fabricacao}"
        f" por {product.nome_da_empresa} com validade"
        f" até {product.data_de_validade}"
        f" precisa ser armazenado {product.instrucoes_de_armazenamento}."
    )
