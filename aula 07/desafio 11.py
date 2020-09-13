altura = float(input('Insira a altura da parede: '))
largura = float(input('Insira a largura da parede '))
area = altura * largura
qtd_tinta = area / 2
print('A area da parede é de {}'.format(area), end= '')
print('e a quantidade de tinta necessária para pintar é de {}L'.format(qtd_tinta))
