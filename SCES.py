# [ID do Produto (numérico), Nome do Produto (texto), Quantidade em Estoque (numérico), Localização
produtos = [
    [5864, "Cabos", 350, "Pratileira B-02-12"],
    [7856, "Parafuso", 400, "Pratileira C-06-24"],
    [9680, "Fitas", 180, "Pratileira H-05-36"],
    [2851, "Prego", 536, "Pratileira V-07-48"],
    [4683, "Porca", 620, "Pratileira L-01-60"]
]

def status():
    print("\n------------- STATUS DO ESTOQUE -------------")
    for prod in produtos:
        print(f"ID: {prod[0]} | Nome: {prod[1]} | Qtd: {prod[2]} | Local: {prod[3]}")
    print("---------------------------------------------\n")

def registrar_novo_produto():
    print("\n---------------------------------------------\n")
    print("\n--- Registrar Novo Produto ---")
    id_prod = int(input("Insira o ID do produto (numérico): "))
    nome = input("Insira o nome do produto: ")
    qtd = int(input("Insira a quantidade em estoque: "))
    local = input("Insira a localização no estoque: ")

    if id_prod or nome or local == produtos:
      print("Você não pode registrar um produto com informações similares a um produto existente!") 

    else:   
        produtos.append([id_prod, nome, qtd, local])
        print("Novo produto inserido com sucesso!\n")
    
    print("\n---------------------------------------------\n")

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

def novo_estoque():
   print("\n---------------------------------------------\n")

   print("Certo! a quantidade de um produto será mudada!\n")
   ("Primeiro, me informe qual produto você gostaria de mudar por seu ID")

print("---------------------------------------------\n")
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
        print("Opção inválida! Tente novamente.\n")