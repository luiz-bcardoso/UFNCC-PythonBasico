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
instrucao = '00100011'  # (2bit x 4)


def mostraMemoria():
    global memoria
    mem = ''
    for p in memoria:
        mem += p
    print(mem)


def mostraAcc():
    print(f'ACC: {acc}')


def ler(pos):
    global acc
    acc = memoria[pos]
    mostraAcc()


def escrever(pos, dado):
    global acc, memoria
    memoria[pos] = dado
    mostraMemoria()


def soma(pos1, pos2):
    pass


def sub(pos1, pos2):
    pass


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
        ler(endDec)
    if comDec == 1:
        escrever(endDec, dado)
    if comDec == 2:
        soma(0,0)
    if comDec == 3:
        sub(0,0)


# bin to dec
print(int('1111', 2))

mostraMemoria()
ler(1)
escrever(3, '1100')

print(instrucao)
executaInstrucao(instrucao)
