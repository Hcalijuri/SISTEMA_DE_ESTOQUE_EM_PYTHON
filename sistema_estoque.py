
# Sistema de Gerenciamento de Estoque em Python

estoque = {}
id_atual = 1
estoque_minimo = 4

def menu():
    print("\n==== MENU PRINCIPAL ====")
    print("1. Cadastrar Produto")
    print("2. Editar Produto")
    print("3. Remover Produto")
    print("4. Registrar Entrada de Produto")
    print("5. Registrar Saída de Produto")
    print("6. Consultar Produto")
    print("7. Relatório Geral")
    print("8. Relatório de Baixo Estoque")
    print("0. Sair")

def cadastrar_produto():
    global id_atual
    nome = input("Nome do produto: ")
    categoria = input("Categoria: ")
    try:
        quantidade = int(input("Quantidade em estoque: "))
        preco = float(input("Preço: R$ "))
        estoque[id_atual] = {
            'nome': nome,
            'categoria': categoria,
            'quantidade': quantidade,
            'preco': preco
        }
        print(f"Produto cadastrado com ID: {id_atual}")
        id_atual += 1
    except ValueError:
        print("Entrada inválida! Cadastro cancelado.")

def editar_produto():
    try:
        id_prod = int(input("ID do produto a editar: "))
        if id_prod in estoque:
            nome = input("Novo nome (deixe vazio para manter): ")
            categoria = input("Nova categoria (deixe vazio para manter): ")
            qtd = input("Nova quantidade (deixe vazio para manter): ")
            preco = input("Novo preço (deixe vazio para manter): ")

            if nome:
                estoque[id_prod]['nome'] = nome
            if categoria:
                estoque[id_prod]['categoria'] = categoria
            if qtd:
                estoque[id_prod]['quantidade'] = int(qtd)
            if preco:
                estoque[id_prod]['preco'] = float(preco)

            print("Produto atualizado com sucesso!")
        else:
            print("Produto não encontrado.")
    except ValueError:
        print("Entrada inválida.")

def remover_produto():
    try:
        id_prod = int(input("ID do produto a remover: "))
        if id_prod in estoque:
            del estoque[id_prod]
            print("Produto removido com sucesso.")
        else:
            print("Produto não encontrado.")
    except ValueError:
        print("Entrada inválida.")

def registrar_entrada():
    try:
        id_prod = int(input("ID do produto para entrada: "))
        if id_prod in estoque:
            qtd = int(input("Quantidade a adicionar: "))
            estoque[id_prod]['quantidade'] += qtd
            print("Entrada registrada.")
        else:
            print("Produto não encontrado.")
    except ValueError:
        print("Entrada inválida.")

def registrar_saida():
    try:
        id_prod = int(input("ID do produto para saída: "))
        if id_prod in estoque:
            qtd = int(input("Quantidade a retirar: "))
            if qtd <= estoque[id_prod]['quantidade']:
                estoque[id_prod]['quantidade'] -= qtd
                print("Saída registrada.")
            else:
                print("Estoque insuficiente!")
        else:
            print("Produto não encontrado.")
    except ValueError:
        print("Entrada inválida.")

def consultar_produto():
    termo = input("Buscar por nome, categoria ou ID: ").lower()
    try:
        id_busca = int(termo)
        if id_busca in estoque:
            print(f"{id_busca}: {estoque[id_busca]}")
        else:
            print("Produto não encontrado.")
    except ValueError:
        encontrados = [f"{id}: {prod}" for id, prod in estoque.items()
                       if termo in prod['nome'].lower() or termo in prod['categoria'].lower()]
        if encontrados:
            for item in encontrados:
                print(item)
        else:
            print("Produto não encontrado.")

def relatorio_geral():
    print("\n=== RELATÓRIO GERAL ===")
    for id, produto in estoque.items():
        print(f"{id}: {produto}")

def relatorio_baixo_estoque():
    print("\n=== PRODUTOS COM BAIXO ESTOQUE ===")
    for id, produto in estoque.items():
        if produto['quantidade'] < estoque_minimo:
            print(f"{id}: {produto}")

# Execução principal
while True:
    menu()
    opcao = input("Escolha uma opção: ")
    if opcao == '1':
        cadastrar_produto()
    elif opcao == '2':
        editar_produto()
    elif opcao == '3':
        remover_produto()
    elif opcao == '4':
        registrar_entrada()
    elif opcao == '5':
        registrar_saida()
    elif opcao == '6':
        consultar_produto()
    elif opcao == '7':
        relatorio_geral()
    elif opcao == '8':
        relatorio_baixo_estoque()
    elif opcao == '0':
        print("Saindo do sistema.")
        break
    else:
        print("Opção inválida. Tente novamente.")
