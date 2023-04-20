
UnidadesdeArmazenamento = ['Bit','Byte','kilobyte', 'Megabyte', 'Gigabyte','Terabyte','Petabyte']


print('coloque a Sua unidade de armazenamneto inicial:')
Unidade = input()
print('selecione o seu valor inicial:')
ValorInicial = input()
print('você quer converter para:')
Convertido = input()
print('selecione o seu valor Final:')
ValorFinal = input()


def Conversão(valor):
    contador = 0
    for i in UnidadesdeArmazenamento:
        contador += 1
        print(contador)




