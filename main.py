habitos = []


def criar_habito(lista):
    while True:
        nome_habito = str(input("Digite o nome do hábito: ")).strip()
        if not nome_habito:
            print("Digite um hábito!")
        else:
            print("Hábito criado")
            habito = {'nome': nome_habito, 'Progresso': "Pendente"}
            lista.append(habito)
            break


def listar_habitos(lista):
    concluido = 0
    print("HÁBITOS:")
    for i, habito in enumerate(lista):
        status = f"{i + 1}. {habito['nome']} - {habito['Progresso']}"
        if habito['Progresso'] == "Pendente":
            print(status)
        else:
            print(status)
            concluido += 1
    print(f"{concluido} concluído(s) de {len(lista)}")


def concluir_habito(lista):
    print("Habitos pendentes")

    for i, habito in enumerate(lista):
        print(f"{i + 1}. {habito['nome']} - {habito['Progresso']}")
    escolha = int(input("Digite de acordo com a posição: ")) - 1
    if 0 <= escolha < len(lista):
        if lista[escolha]['Progresso'] == "Concluido":
            print("Esse hábito já está concluído!")
        else:
            print("Hábito Concluído!")
            lista[escolha]['Progresso'] = "Concluido"
    else:
        print("Digite uma posição válida!")


def deletar_habito(lista):
    listar_habitos(lista)
    escolha = int(input("De acordo com a posição escolha qual deseja apagar: ")) -1
    if 0 <= escolha < len(lista):

        lista.pop(escolha)
        print("Deletado com sucesso!!")
    else:
        print("Digite um indice válido!")


def main():
    while True:
        print("\n" + "=" * 30)
        print(" GERENCIADOR DE HÁBITOS ".center(30, "="))
        print("[1] Criar Hábito")
        print("[2] Listar Hábitos")
        print("[3] Concluir Hábito")
        print("[4] Deletar Hábito")
        print("[0] Sair")
        print("=" * 30)

        try:
            escolha_user = int(input("Digite o que deseja: "))
        except ValueError:
            print("Digite um número válido!")
            continue

        if escolha_user == 1:
            criar_habito(habitos)
        elif escolha_user == 2:
            listar_habitos(habitos)
        elif escolha_user == 3:
            concluir_habito(habitos)
        elif escolha_user == 4:
            deletar_habito(habitos)
        elif escolha_user == 0:
            break



main()
