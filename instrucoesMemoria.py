#Programação de Sistemas, 17/09/2024
def memoriaCool():
    memoria = [0 for i in range(8)]
    print(memoria)
    tamanho = 8

    if len(memoria) > tamanho:
        raise Exception(f'Items exceeds the maximum allowed length of {tamanho}')

    if memoria.count(1) + memoria.count(0) != len(memoria):
        raise Exception(f'Memory contains a non-binary value.')


memoria = ['1000', '1111', '0101', '1010']
acc = ['0000']
# 00 = read
# 01 = write    
# 10 = sum
# 11 = sub
instrucao = '10100101'  # (2bit x 4)


def mostraMemoria():
    global memoria
    mem = ''
    for p in memoria:
        mem += p
    print(mem)


def mostraAcc():
    print(f'ACC: {acc} ({int(acc, 2)})')


def ler(pos):
    global acc
    acc = memoria[pos]
    mostraAcc()


def escrever(pos, dado):
    global acc, memoria
    memoria[pos] = dado
    mostraMemoria()


def soma(regX, valor):
    global acc
    ler(regX)
    #print('ACC(Dec)',int(acc, 2))
    print(f'VAL: {valor} ({int(valor, 2)})')
    res = str(bin(int(acc, 2) + int(valor, 2))[2:])
    #Checks for a value greater than 4 bits
    if len(res) > 4:
        print('RES: Buffer Overflow ')
        res = '0000'
    else:
        acc = f'{res}' #removes 2b
    acc = corrigeBinario(acc)
    mostraAcc()
    #print(f'regX:{regX}, acc:{acc}')
    escrever(regX, acc)


def sub(regX, valor):
    global acc
    ler(regX)
    print(f'VAL: {valor} ({int(valor, 2)})')
    acc = f'{int(bin(int(acc, 2) - int(valor, 2))[2:])}' #removes 2b
    acc = corrigeBinario(acc)
    mostraAcc()
    escrever(regX, acc)


def mult(regX, valor):
    global acc
    res = 0

    ler(regX)
    print(f'VAL: {valor} ({int(valor, 2)})')

    #Sum the same value in acc for x times 'valor'
    for i in range(int(valor, 2)):
        res += int(acc, 2)

    #Add 'res' to 'acc'
    acc = str(bin(res)[2:])
    corrigeBinario(acc)
    mostraAcc()

    # Checks for a value greater than 4 bits
    if len(acc) > 4:
        print('RES: Buffer Overflow ')
        acc = '0000'
    else:
        acc = f'{res}'

    escrever(regX, acc)

def corrigeBinario(acc):
    tamanhoRes = len(acc)
    if tamanhoRes < 4:
        for i in range(4-tamanhoRes):
            acc = '0'+acc
    return acc


def executaInstrucao(instr):
    com = instr[:2]  # corta do primeiro ao 2
    comDec = int(com, 2)
    end = instr[2:4]  # corta do 2 ao 4
    endDec = int(end, 2)
    dado = instr[4:]  # corta do 4 ao ultimo
    dadoDec = int(dado, 2)

    print(f'Binary [{com} {end} {dado}]')
    print(f'Decimal [{comDec} {endDec} {dadoDec}]')

    if comDec == 0:
        print(f'READ register #{endDec}')
        ler(endDec)
    if comDec == 1:
        print(f'WRITE register #{endDec} VALUE {dado}')
        escrever(endDec, dado)
    if comDec == 2:
        print(f'SUM register #{endDec} VALUE {dado}')
        input_value = input('Deseja multiplicar um valor por outro ao inves da soma? (Y/N): ')
        mostraMemoria()
        if input_value.upper() == 'Y':
            mult(endDec, dado)
        else:
            soma(endDec, dado)
    if comDec == 3:
        print(f'SUB register #{endDec} VALUE {dado}')
        mostraMemoria()
        sub(endDec,dado)

# bin to dec
#print(int('1111', 2))

mostraMemoria()
ler(1)
escrever(3, '1100')

print(instrucao)
executaInstrucao(instrucao)