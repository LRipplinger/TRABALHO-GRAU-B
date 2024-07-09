import csv
from datetime import datetime

# Função principal do programa:
def main():
    filename = "felinos.csv"  
    felinos = carregar_dados(filename)  
    
    while True:
        print("\nMenu Principal:")  
        print("1) Cadastrar felino")
        print("2) Alterar status de felino")
        print("3) Consultar informações sobre felino")
        print("4) Apresentar estatísticas gerais")
        print("5) Filtragem de dados")
        print("6) Salvar")
        print("7) Sair do programa")
        opcao = int(input("Escolha uma opção: "))  
        
        if opcao == 1:
            cadastrar_felino(felinos)  
        elif opcao == 2:
            alterar_status(felinos)  
        elif opcao == 3:
            consultar_felino(felinos)  
        elif opcao == 4:
            apresentar_estatisticas(felinos)  
        elif opcao == 5:
            filtrar_dados(felinos)  
        elif opcao == 6:
            salvar_dados(filename, felinos)  
            print("Dados salvos com sucesso!")
        elif opcao == 7:
            salvar_dados(filename, felinos)  
            print("Saindo do programa... Dados foram salvos com sucesso!!!")
            break  
        else:
            print("Opção inválida!!!.")  

# Função que carrega dados do arquivo CSV
def carregar_dados(filename):
    felinos = []  
    try:
        # Função que abre o arquivo CSV
        with open(filename, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)  
            for row in reader:
                felinos.append(row)  
    except FileNotFoundError:
        print(f"Arquivo {filename} não encontrado!!!.")  
    return felinos  

# Função que salva os dados no arquivo CSV:
def salvar_dados(filename, felinos):
    with open(filename, mode='w', encoding='utf-8', newline='') as file:
        fieldnames = felinos[0].keys()  
        writer = csv.DictWriter(file, fieldnames=fieldnames)  
        writer.writeheader()  
        writer.writerows(felinos)  

# Função para gerar um ID para o felino:
def gerar_id(felinos):
    return str(len(felinos) + 1)  #

# Função para cadastrar um novo felino:
def cadastrar_felino(felinos):
    felino = {  
        "ID": gerar_id(felinos),  
        "Nome": input("Nome: "),  
        "Sexo": input("Sexo (M/F): "),  
        "Idade": input("Idade: "),  
        "Raça": input("Raça: "),  
        "Cor Predominante": input("Cor Predominante: "),  
        "Castrado": input("Castrado (Sim/Não): "),  
        "FIV+": input("FIV+ (Sim/Não): "),  
        "FELV+": input("FELV+ (Sim/Não): "),  
        "Data de Resgate": input("Data de Resgate (dd/mm/yyyy): "),  
        "Adotado": input("Adotado (Sim/Não): "),  
        "Lar Temporário": input("Lar Temporário: "),  
        "Adoção/Hospedagem": input("Adoção/Hospedagem: "),  
        "Tutor": input("Tutor: "),  
        "Contato": input("Contato: "),  
        "Data Última Vacina": input("Data Última Vacina (dd/mm/yyyy): "),  
        "Data Última Desvermifugação": input("Data Última Desvermifugação (dd/mm/yyyy): "),  
        "Data Último Antipulgas": input("Data Último Antipulgas (dd/mm/yyyy): "),  
        "Informações Extras": input("Informações Extras: ")  
    }
    felinos.append(felino)  
    # Informa que o felino foi cadastrado com sucesso:
    print("Felino cadastrado com sucesso!!!")  

# Função que altera os status do felino:
def alterar_status(felinos):
    listar_felinos:(felinos)  
    id_felino = input("Escolha o ID do felino que deseja alterar!!!: ")  
    felino = next((f for f in felinos if f["ID"] == id_felino), None)  
    if felino:
        print("Informações do felino!:")  
        for i, (key, value) in enumerate(felino.items()):
            print(f"{i+1}. {key}: {value}")
        while True:
            opcao = int(input("Escolha o número da informação que deseja alterar (0 para sair): "))  
            if opcao == 0:
                break  
            campo = list(felino.keys())[opcao-1]  
            novo_valor = input(f"Novo valor para {campo}: ")  
            felino[campo] = novo_valor  
        print("Informações alteradas com sucesso!!!")  
    else:
        print("Felino não encontrado!!!.")  

# Função que consulta as informaçoes de um felino:
def consultar_felino(felinos):
    listar_felinos:(felinos)  
    id_felino = input("Escolha o ID do Felino!!!: ")  
    felino = next((f for f in felinos if f["ID"] == id_felino), None)  
    if felino:
        print("Informações do felino!!!:")  
        for key, value in felino.items():
            print(f"{key}: {value}")
    else:
        print("Felino não encontrado!!!.")  

# Função que lista todos os felinos:
def listar_felinos(felinos):
    for felino in felinos:
        print(f"ID: {felino['ID']} - Nome: {felino['Nome']}")  

# Função que apresenta as estatisticas gerais dos felinos:
def apresentar_estatisticas(felinos):
    total = len(felinos)  
    machos = sum(1 for f in felinos if f["Sexo"] == "M")  
    femeas = sum(1 for f in felinos if f["Sexo"] == "F")  
    adotados = sum(1 for f in felinos if f["Adotado"] == "Sim")  
    nao_adotados = total - adotados  
    fiv_negativos = sum(1 for f in felinos if f["FIV+"] == "Não" and f["FELV+"] == "Não")  
    fiv_positivos = sum(1 for f in felinos if f["FIV+"] == "Sim" and f["FELV+"] == "Não")  
    felv_positivos = sum(1 for f in felinos if f["FIV+"] == "Não" and f["FELV+"] == "Sim")  
    fiv_felv_positivos = sum(1 for f in felinos if f["FIV+"] == "Sim" and f["FELV+"] == "Sim")  

    print("Estatísticas Gerais:")  
    print(f"Total de felinos: {total}")
    print(f"Porcentagem de machos: {machos / total * 100:.2f}%")
    print(f"Porcentagem de fêmeas: {femeas / total * 100:.2f}%")
    print(f"Porcentagem de adotados: {adotados / total * 100:.2f}%")
    print(f"Porcentagem de não adotados: {nao_adotados / total * 100:.2f}%")
    print(f"Porcentagem de FIV- e FELV-: {fiv_negativos / total * 100:.2f}%")
    print(f"Porcentagem de apenas FIV+: {fiv_positivos / total * 100:.2f}%")
    print(f"Porcentagem de apenas FELV+: {felv_positivos / total * 100:.2f}%")
    print(f"Porcentagem de FIV+ e FELV+: {fiv_felv_positivos / total * 100:.2f}%")

# Função que filtra os dados dos felinos:
def filtrar_dados(felinos):
    print("1) Consultar gatos resgatados por ano")  
    print("2) Consultar gatos adotados por ano")  
    opcao = int(input("Escolha uma opção: "))  
    ano_inicio = int(input("Ano de início: "))  
    ano_fim = int(input("Ano de fim: "))  
    
    if opcao == 1:
        resgatados = [f for f in felinos if ano_inicio <= datetime.strptime(f["Data de Resgate"], "%d/%m/%Y").year <= ano_fim]  # filtra os felinos resgatados no período
        print(f"Gatos resgatados entre {ano_inicio} e {ano_fim}:")  
        for felino in resgatados:
            print(f"ID: {felino['ID']} - Nome: {felino['Nome']} - Data de Resgate: {felino['Data de Resgate']}")
    elif opcao == 2:
        adotados = [f for f in felinos if f["Adotado"] == "Sim" and ano_inicio <= datetime.strptime(f["Data de Resgate"], "%d/%m/%Y").year <= ano_fim]  # filtra os felinos adotados no período
        print(f"Gatos adotados entre {ano_inicio} e {ano_fim}:")  
        for felino in adotados:
            print(f"ID: {felino['ID']} - Nome: {felino['Nome']} - Data de Resgate: {felino['Data de Resgate']}")
    else:
        print("Opção inválida.")  

if __name__ == "__main__":
    main()
