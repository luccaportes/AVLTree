from tree import Tree
from os import system, name


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

        # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


while True:
    opt = input("O que deseja fazer?\n1 - Inserir\n2 - Remover ")
    number = input("Digite o número (Serão convertidos para inteiros): ")
    try:
        number = int(number)
    except ValueError:
        print("Numero inválido")
        continue
    if opt == "1":
        tree.insert(number)
    elif opt == "2":
        tree.delete(number)
    else:
        print("Opção inválida")
        continue
    tree.display()
    input("Aperte enter para continuar")
    clear()






