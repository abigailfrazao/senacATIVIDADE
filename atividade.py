def venda_de_produto():
    """
    Função para realizar a venda de um produto.
    """
    print("*************Venda de produto*********")

    while True:
        nome_produto = input("Escreva o nome do produto: ")
        try:
            preco = float(input("Escreva o preço: "))
            quantidade = int(input("Escreva a quantidade: "))
            break  
        except ValueError:
            print("Atenção! Os campos 'quantidade' e 'preço' devem conter apenas valores numéricos.")
            print("Tente novamente!")

    valor_total = preco * quantidade
    print(f"Valor a pagar: {valor_total:.1f}")

    while True:
        try:
            metodo_pagamento = int(input("Escolha o método de pagamento: 1. dinheiro 2.pix 3. cartão (crédito/débito) - "))
            if metodo_pagamento in [1, 2, 3]:
                break  
            else:
                print("Método de pagamento inválido. Escolha entre 1, 2 ou 3.")
        except ValueError:
            print("Entrada inválida. Digite 1, 2 ou 3.")

    if metodo_pagamento == 1:
        print("-> Você escolheu dinheiro. Pagamento realizado em dinheiro.")
    elif metodo_pagamento == 2:
        print("-> Você escolheu pix. Pagamento realizado via pix.")
    else:
        print("-> Você escolheu cartão. Pagamento realizado no cartão (crédito/débito).")

    print("Volte logo, esperamos por você!")

venda_de_produto()
venda_de_produto()