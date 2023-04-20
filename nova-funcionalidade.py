UnidadesDeArmazenamento = ['Bit', 'Byte', 'Kilobyte', 'Megabyte', 'Gygabyte', 'Terabyte', 'Petabyte' ]

def mostrarUnidadesDeMedida(UnidadesDeArmazenamento):
    print('Unidades de Medida Disponíveis:')
    for i in UnidadesDeArmazenamento:
        print(i)

def calcularFatorDeConversão(ValorInicial, ValorParaConversão):
    contador = 0
    for i in UnidadesDeArmazenamento:
        if (ValorInicial == i):
            ValorInicial = contador

        if (ValorParaConversão == i):
            ValorParaConversão = contador

        contador += 1
    FatorParaConversão = ValorInicial - ValorParaConversão
    return int(FatorParaConversão)

def conversão(ValorInicial, ValorParaConversão, NúmeroDeConversão):
    FatorParaConversão = calcularFatorDeConversão(ValorInicial, ValorParaConversão)
    númeroConvertido = NúmeroDeConversão

    if(ValorInicial == 'Bit' or ValorParaConversão == 'Bit'):
        if(ValorInicial == 'Bit'):
            númeroConvertido /= 8
            FatorParaConversão += 1 
        if(ValorParaConversão == 'Bit'):
            númeroConvertido *= 8 
            FatorParaConversão -= 1 

    if (FatorParaConversão < 0):
        FatorParaConversão *= -1
        FatorParaConversão = 1024 ** FatorParaConversão
        númeroConvertido /= FatorParaConversão
    elif(FatorParaConversão > 0):
        FatorParaConversão = 1024 ** FatorParaConversão
        númeroConvertido *= FatorParaConversão
        
    return númeroConvertido

mostrarUnidadesDeMedida(UnidadesDeArmazenamento)

print('Digite a unidade de medida inicial do valor:')
ValorInicial = input()
print('Digite a unidade para qual o valor será convertido:')
ValorParaConversão = input()
print('Digite o número a ser convertido:')
numeroParaConversão = float(input())

print('Resultado da conversão:')
print(str(conversão(ValorInicial, ValorParaConversão, numeroParaConversão)) + ' ' + ValorParaConversão + 's')
