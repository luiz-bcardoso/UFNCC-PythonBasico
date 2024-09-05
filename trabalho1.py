#Nome: Luiz 'Xiru' Batista Cardoso
#Atividade: Programa em Python que receba nomes de pessoas, transforme para maisculo e insira em uma lista sem repetição. Além disso o programa deve criar automaticamente uma lista de e-mails com dominio "@ufn.edu.br" adicionar por nome.
lista_pessoas = []
lista_emails = []
while True:
    nome = input('Digite o nome de uma pessoa: ')
    if(nome not in lista_pessoas):
        lista_pessoas.append(nome.upper())
        lista_emails.append(nome.replace(" ", "")+"@ufn.edu.br")

    resp = input(f"Deseja cadastrar outra pessoa? (S/N)").upper()
    if "S" not in resp:
        break;
    print(lista_pessoas)

#Ordena e exibe a lista
print('Listas ordenadas')
lista_pessoas.sort()
lista_emails.sort()
print(lista_pessoas)
print(lista_emails)
