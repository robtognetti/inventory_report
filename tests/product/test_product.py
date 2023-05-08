from inventory_report.inventory.product import Product


def test_cria_produto():
    product = Product(
        id=1,
        nome_do_produto="Produto any",
        nome_da_empresa="Empresa any",
        data_de_fabricacao="2027-09-11",
        data_de_validade="2029-04-09",
        numero_de_serie="j4b1l3u",
        instrucoes_de_armazenamento="seco e fresco"
    )
    assert product.id == 1
    assert product.nome_do_produto == "Produto any"
    assert product.nome_da_empresa == "Empresa any"
    assert product.data_de_fabricacao == "2027-09-11"
    assert product.data_de_validade == "2029-04-09"
    assert product.numero_de_serie == "j4b1l3u"
    assert product.instrucoes_de_armazenamento == "seco e fresco"
