# [ID do Produto (numérico), Nome do Produto (texto), Quantidade em Estoque (numérico), Localização]


produtos = [ 
    [5864, "Cabos", 350, "B-02-12"], 
    [7856, "Parafuso", 400, "C-06-24"], 
    [9680, "Fitas", 180, "H-05-36"], 
    [2851, "Prego", 536, "V-07-48"], 
    [4683, "Porca", 620, "L-01-60"] 
]


# Função de mostrar o status do estoque


def status():
    print("\n------------- STATUS DO ESTOQUE -------------")
    for prod in produtos:
        print(f"ID: {prod[0]} | Nome: {prod[1]} | Qtd: {prod[2]} | Local: Pratileira {prod[3]}")
    print("---------------------------------------------\n")


# Função de registrar novo produto


def registrar_novo_produto():
    print("\n---------------------------------------------\n")
    print("\n--- Registrar Novo Produto ---")
    id_prod = int(input("Insira o ID do produto (numérico): "))
    nome = input("Insira o nome do produto: ")
    qtd = int(input("Insira a quantidade em estoque: "))
    local = input("Insira a localização no estoque (ex: A-08-05): ")
    
    id_existe = False
    for prod in produtos:
        if prod[0] == id_prod:
            id_existe = True
            break

    if id_existe:
        print("Você não pode registrar um produto com informações similares a um produto existente!")
    else:
        produtos.append([id_prod, nome, qtd, local])
        print("Novo produto inserido com sucesso!\n")
    print("\n---------------------------------------------\n")


#Função de Buscar por ID


def produto_ID():
    print("\n---------------------------------------------\n")
    print("\n--- Buscar Produto por ID ---")
    id_procurado = int(input("Digite o ID do produto: "))
    for prod in produtos:
        if prod[0] == id_procurado:
            print(f"Produto encontrado: {prod[1]} | Estoque: {prod[2]} | Local: {prod[3]}\n")
            print("\n---------------------------------------------\n")
            return 

    print("Produto não encontrado no estoque.\n")
    print("\n---------------------------------------------\n")


# Função de mudar quantidade de um produto


def novo_estoque():
    print("\n---------------------------------------------\n")
    print("Certo! a quantidade de um produto será mudada!\n")
    id_procurado = int(input("Primeiro, me informe qual produto você gostaria de mudar por seu ID: "))
    
    for prod in produtos:
        if prod[0] == id_procurado:
            print(f"Produto selecionado: {prod[1]} (Estoque atual: {prod[2]})")
            print("1 - Entrada (Adicionar) | 2 - Saída (Remover)")
            operacao = input("Escolha a operação: ")
            
            if operacao == "1":
                quantidade = int(input("Quantidade de entrada: "))
                prod[2] += quantidade
                print(f"Entrada realizada! Novo estoque de {prod[1]}: {prod[2]}")
            elif operacao == "2":
                quantidade = int(input("Quantidade de saída: "))
                if quantidade <= prod[2]:
                    prod[2] -= quantidade
                    print(f"Saída realizada! Novo estoque de {prod[1]}: {prod[2]}")
                else:
                    print("Erro: Quantidade de saída maior do que o estoque disponível!")
            else:
                print("Operação inválida!")
                
            print("---------------------------------------------\n")
            return
            
    print("Produto não encontrado.")
    print("---------------------------------------------\n")


#Menu do estoque
print("Bem vindo ao menu de controle de estoque!\n")

print("Por favor, selecione uma das opões a seguir para começarmos: \n")

while True:
    print("1- Adicionar produto | 2- Listar produtos | 3- Buscar por ID | 4- Atualizar Estoque | 5- Sair")
    opção = input("Escolha uma opção: ")
    print("\n---------------------------------------------\n")
    
    if opção == "1":
        registrar_novo_produto()
    elif opção == "2":
        status()
    elif opção == "3":
        produto_ID()
    elif opção == "4":
        novo_estoque()
    elif opção == "5":
        print("Interação encerrada.")
        break
    else:
        print("Opção inválida. Tente novamente.")
