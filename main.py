import Utils
import exercicios.calcularIMC

def main():
    print(f"Selecione um dos exercícios abaixo:")
    escolhas = ['1. Caluclar IMC',
                '2. TBA']
    Utils.listarLista(escolhas)
    escolha = input(f"Selecione uma opção: ")
    escolher_exercicio(escolha)
              
def escolher_exercicio(opt):
    if(opt is '1'):
        exercicios.calcularIMC.__main__()
        return 0
    elif(opt is '2'):
        print(f"Exercício ainda não foi implementado...")
        return 0
    else:
        print(f"Digite uma opção válida...")
        return 0

main()
