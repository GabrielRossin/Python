n1 = int(input('Um valor:'))
n2 = int(input('Outro valor'))
soma = n1+n2
multi = n1 * n2
div = n1/n2
div_int = n1 // n2
exp = n1 ** n2
print('A soma vale {}; '.format(soma),end=' ')
print('O produto vale {}; '.format(multi),end= ' ')
print('A divisão vale {:.3f}; '.format(div),end= ' ')
print('A divisão inteira vale {}; '.format(div_int),end= ' ')
print('A potência vale {}'.format(exp))