def obter_nome():
    """Obtém o nome do usuário e garante que não esteja vazio."""
    while True:
        nome = input('Digite o nome de uma pessoa: ').strip()
        if nome:
            return nome
        print("O nome não pode ser vazio. Por favor, tente novamente.")

def cadastrar_pessoas():
    """Cadastra pessoas e seus e-mails em listas."""
    lista_pessoas = []
    lista_emails = []

    while True:
        nome = obter_nome()
        nome_upper = nome.upper()
        
        if nome_upper not in lista_pessoas:
            lista_pessoas.append(nome_upper)
            email = f"{nome.replace(' ', '')}@ufn.edu.br"
            lista_emails.append(email)
        
        resp = input("Deseja cadastrar outra pessoa? (S/N): ").strip().upper()
        if resp != 'S':
            break

    return lista_pessoas, lista_emails

def exibir_listas(lista_pessoas, lista_emails):
    """Ordena e exibe as listas de pessoas e e-mails."""
    lista_pessoas.sort()
    lista_emails.sort()
    
    print('Listas ordenadas:')
    print(f'Pessoas: {lista_pessoas}')
    print(f'E-mails: {lista_emails}')

def main():
    """Função principal para execução do programa."""
    lista_pessoas, lista_emails = cadastrar_pessoas()
    exibir_listas(lista_pessoas, lista_emails)

if __name__ == "__main__":
    main()
