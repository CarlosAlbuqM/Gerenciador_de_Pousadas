import os 

usuarioLogado = False
usuarios = [
        ["Carlos", "123456"],
        ["Lucas", "10000"],
        ["Manuela","321"],
        ["Larissa", "222222"]
]
listaPousada = [ 
        {"nome": "Pousada Viking", "diaria": 40.00, "cidade": "Maceió","quartos_disp": 10,},
        {"nome": "Pousada Raio de Sol", "diaria": 10.00,"cidade": "Recife","quartos_disp": 50,},
        {"nome": "Pousada Mar Aberto", "diaria": 120.00,"cidade": "Aracaju","quartos_disp": 2,},
        {"nome": "Pousada Tio Patinha", "diaria": 30.00,"cidade": "Manaus","quartos_disp": 16,},
        {"nome": "Hostel do amor", "diaria": 223.00,"cidade": "Garanhuns","quartos_disp": 12,},
        {"nome": "Pousada do Rei", "diaria": 23.00,"cidade": "Bahia","quartos_disp": 24,},
        {"nome": "Pousada Bula", "diaria": 92.00,"cidade": "São Paulo","quartos_disp": 43,}
        ]

def pause():
    input("Pressione ENTER para continuar...\n")

def login():
    global usuarioLogado
    nome_usuario = input("Digite seu nome de usuário: ")

    for usuario in usuarios:
        if usuario[0] == nome_usuario:
            senha = input("Digite sua senha: ")
            if usuario[1] == senha:
                print(f" -- Bem-vindo, {nome_usuario}!--\n")
                usuarioLogado = True
                pause()
                os.system('cls')
                return True
            else:
                print ("Senha incorreta. Tente novamente\n")
                return  False
                
    cad_usuario=input("Usário não cadastrado. deseja cadastrar um novo usuário. (S/N)?  ").upper()
    if cad_usuario == 'S':
        cadastrar()
    else:
        return False
    

def cadastrar():
    print("\n")
    print(" -- CADASTRO DE USUÁRIO --\n")
    nome_usuario = input("Digite seu nome de usuário: ")
    senha = input("Digite sua Senha: ")

    for usuario in usuarios:
        if usuario[0] == nome_usuario:
            print("Nome de usuário já cadastrado. Tente outro. \n" )
            return False
    
    usuarios.append ([nome_usuario, senha])
    print(f"Usuário {nome_usuario}, foi cadastrado com sucesso.")
    pause()
    os.system('cls')

def cad_pousada():
    print("\n")
    print (" -- CADASTRO DE POUSADA --\n\n")
    nome = input("Digite o nome da pousada que gostaria de cadastrar: \n")
    diaria = float(input("Digite o preço da diária: R$ "))
    cidade = input("Digite a cidade onde a pousada fica localizada: ")
    quartos_disp = int(input("Digite a quantidade de quartos que estão disponíveis: "))

    pousada = {
        "nome": nome,
        "diaria": diaria,
        "cidade": cidade,
        "quartos_disp": quartos_disp
    }

    listaPousada.append(pousada)
    print(" -  SUA POUSADA FOI CADASTRADA COM SUCESSO  -  \n")    
    pause()
    os.system('cls')
    
    
def bus_pousada():
    print("\n")
    print(" -- BUSCAR POUSADA --\n")
    buscarpousada = input("Você deseja buscar uma pousada por cidade ou preço? C/P: ").upper()
    
    if buscarpousada == "C":
        encontrou_pousada = False
        while not encontrou_pousada:
            cidade = input("Digite a cidade desejada: \n")
            for pousada in listaPousada:
                if pousada["cidade"] == cidade:
                    print(f"Nome: {pousada['nome']}\nPreço: R$ {pousada['diaria']}\nCidade: {pousada['cidade']}\nQuartos Disponíveis: {pousada['quartos_disp']}\n\n")
                    encontrou_pousada = True
                    break
            if not encontrou_pousada:
                print("Não existe nenhuma pousada disponível nesta cidade. Tente novamente.")
    
    elif buscarpousada == "P":
        preco_Min = float(input("Digite o preço mínimo da diária: "))
        preco_Max = float(input("Digite o preço máximo da diária: "))
        encontrou_pousada = False
        for pousada in listaPousada:
            if preco_Min <= pousada["diaria"] <= preco_Max:
                print(f"Nome: {pousada['nome']}\nPreço: R${pousada['diaria']}\nCidade: {pousada['cidade']}\nQuartos Disponíveis: {pousada['quartos_disp']}\n\n")
                encontrou_pousada = True
        if not encontrou_pousada:
            print("Não existe nenhuma pousada disponível nesta faixa de preço.")

    if encontrou_pousada:
        alugarQuarto = input("Você deseja alugar um quarto (S/N)? ").upper()
        if alugarQuarto == "S":
            alug_quarto()
        else:
            pause()
            os.system('cls')

def alug_quarto():
    print("\n")
    print(" -- ALUGAR QUARTO -- \n")
    nome_p = input("Informe o nome da Pousada na qual gostaria de se hospedar: \n")

    for pousada in listaPousada:
        if pousada["nome"] == nome_p:
            try:
                quartos = int(input("Quantos quartos você gostaria de alugar? "))
                dias = int(input("Quantos dias você vai ficar hospedado? "))
                if quartos <= pousada["quartos_disp"]:
                    pousada["quartos_disp"] -= quartos
                    total = quartos * pousada["diaria"] * dias
                    print(f"Sua reserva foi realizada! Total a pagar: R${total:.2f}")
                    pause()
                    return True
                else:
                    print("Essa quantidade de quartos não está disponível.")
                    return
            except ValueError:
                print("Valor inválido. Digite apenas números.")
                return 
    print("Pousada não está cadastrada no sistema.")
    pause()
    os.system('cls')
     
while True:
    try:
        print("\n")
        print(" --- Bem Vindo ao PouGestor ---\n")
        print("Escolha uma das opções abaixo \n")
        print("1 - Login \n")
        print("2 - Cadastro de Pousada \n")
        print("3 - Buscar Pousada \n")
        print("4 - Sair \n")
        opc=(int(input("Digite uma opção: ")))
        os.system('cls')

        if opc == 1:
            login()
        elif opc == 2:
            if usuarioLogado:
                cad_pousada()
            else:
                print ("Você precisa estar logado para adicionar uma pousada.")
                pause()
        elif opc == 3:
            if usuarioLogado:
                bus_pousada()
            else:
                print ("Você precisa estar logado para buscar pousadas.")
                pause()
        if opc == 4:
            print("Até mais") 
            break
    except ValueError:
        print("Opção inválida. Escolha uma opção de 1-4")


# return (com valor): Pode ser usado para passar um valor de volta ao chamador da função, indicando o sucesso ou o resultado da função.
# return (sem valor): Usado para sair da função sem continuar a execução do código restante.