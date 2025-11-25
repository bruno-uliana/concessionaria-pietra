cliente = {
    "nome": input("Digite seu nome: "),
    "telefone": input("Digite seu telefone: "),
    "saldo": float(input("Digite seu saldo inicial (R$): "))
}


tabela_fipe = {
    "honda civic lxs 1.8 2010": 55000.0,
    "toyota corolla xei 2.0 2013": 62000.0,
    "chevrolet onix 1.0 2019": 48000.0,
    "hyundai hb20 1.6 comfort 2018": 52000.0,
    "volkswagen gol 1.6 2015": 38000.0
}


veiculos_para_aluguel = [
    ("Chevrolet", "Onix 1.0", 2019),
    ("Volkswagen", "Gol 1.6", 2015)
]

veiculos_para_venda = [
    ("Hyundai", "HB20 1.6 Comfort", 2018),
    ("Toyota", "Corolla XEi 2.0", 2013),
    ("Honda", "Civic LXS 1.8", 2010)
]


def menu():
    print("\n===== CONCESSIONÁRIA PYTHON =====")
    print("1 - Vender veículo")
    print("2 - Alugar veículo")
    print("3 - Comprar veículo")
    print("4 - Ver saldo")
    print("0 - Sair")


def vender_veiculo():
    print("\n--- VENDA DE VEÍCULO ---")
    marca = input("Digite a MARCA do veículo: ")
    modelo = input("Digite o MODELO do veículo: ")
    ano = int(input("Digite o ANO do veículo (ex.: 2015): "))

   
    chave = (marca + " " + modelo + " " + str(ano)).lower()

    if chave not in tabela_fipe:
        print("Este veículo não está na tabela FIPE. Venda não realizada.")
        return

    valor_fipe = tabela_fipe[chave]
    proposta = valor_fipe * 0.88 

    print(f"\nValor FIPE: R$ {valor_fipe:.2f}")
    print(f"Proposta da concessionária (FIPE - 12%): R$ {proposta:.2f}")

    confirmacao = input("Deseja vender o veículo? (s/n): ").lower()

    if confirmacao == "s":
        cliente["saldo"] += proposta
        veiculos_para_venda.append((marca, modelo, ano))
        print("Veículo vendido com sucesso!")
    else:
        print("Venda cancelada.")



def alugar_veiculo():
    print("\n--- ALUGUEL DE VEÍCULO ---")

    if not veiculos_para_aluguel:
        print("Não há veículos disponíveis para aluguel.")
        return

    print("\nVeículos disponíveis para aluguel:")
    for i, v in enumerate(veiculos_para_aluguel):
        print(f"{i + 1} - {v[0]} {v[1]} {v[2]}")

    escolha = int(input("Escolha o número do veículo: ")) - 1

    if escolha < 0 or escolha >= len(veiculos_para_aluguel):
        print("Opção inválida.")
        return

    dias = int(input("Por quantos dias deseja alugar? "))
    valor_total = dias * 77

    print(f"Valor total do aluguel: R$ {valor_total:.2f}")

    if cliente["saldo"] < valor_total:
        print("Saldo insuficiente.")
        return

    confirmacao = input("Confirmar aluguel? (s/n): ").lower()
    if confirmacao == "s":
        cliente["saldo"] -= valor_total
        veiculo = veiculos_para_aluguel.pop(escolha)
        print(f"Você alugou '{veiculo[0]} {veiculo[1]} {veiculo[2]}'.")
    else:
        print("Aluguel cancelado.")


def comprar_veiculo():
    print("\n--- COMPRA DE VEÍCULO ---")

    if not veiculos_para_venda:
        print("Não há veículos disponíveis para venda.")
        return

    print("\nVeículos à venda:")
    for i, v in enumerate(veiculos_para_venda):
        print(f"{i + 1} - {v[0]} {v[1]} {v[2]}")

    escolha = int(input("Escolha o número do veículo: ")) - 1

    if escolha < 0 or escolha >= len(veiculos_para_venda):
        print("Opção inválida.")
        return

    marca, modelo, ano = veiculos_para_venda[escolha]

    chave = (marca + " " + modelo + " " + str(ano)).lower()

    if chave not in tabela_fipe:
        print("Veículo sem preço na FIPE. Compra não realizada.")
        return

    valor_fipe = tabela_fipe[chave]
    valor_final = valor_fipe * 1.25  # +25%

    print(f"Valor do veículo (FIPE + 25%): R$ {valor_final:.2f}")

    if cliente["saldo"] < valor_final:
        print("Saldo insuficiente.")
        return

    confirmacao = input("Confirmar compra? (s/n): ").lower()
    if confirmacao == "s":
        cliente["saldo"] -= valor_final
        veiculos_para_venda.pop(escolha)
        print(f"Você comprou '{marca} {modelo} {ano}'.")
    else:
        print("Compra cancelada.")



while True:
    menu()
    opcao = input("Escolha uma opção: ")

    match opcao:
        case "1":
            vender_veiculo()
        case "2":
            alugar_veiculo()
        case "3":
            comprar_veiculo()
        case "4":
            print(f"\nSaldo atual: R$ {cliente['saldo']:.2f}")
        case "0":
            print("Saindo do sistema. Até logo!")
            break
        case _:
            print("Opção inválida. Tente novamente.")
