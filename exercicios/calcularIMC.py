class Pessoa:
    """Classe Pessoa, define dados básicos de usuário

    Parameters:
    nome (str): Nome da pessoa
    altura(float): Altura em metros da pessoa
    peso(float): Peso em quilogramas da pessoa

    Methods:
    calcularIMC(self): Calcula o IMC da pessoa
    """
    def __init__(self, nome, altura, peso):
        self.nome = nome
        self.altura = altura
        self.peso = peso
    
    def calcularIMC(self):
        return (self.peso / (self.altura*self.altura))

def main():
    #Greets the user
    print('Calculo IMC, informe os dados abaixo:')

    #Gather user data
    nome = input('Digite o seu nome completo: ')
    altura = float(input('Digite a sua altura (m): '))
    peso = float(input('Digite o seu peso (kg): '))
    
    #Create new object 'Pessoa' with data
    p1 = Pessoa(nome, altura, peso)

    #Uses 'Pessoa.calulcarIMC' to get person's IMC and prints
    imc = p1.calcularIMC()
    print(f"\nOlá {p1.nome}, seu IMC é {round(imc,2)}.")

main()