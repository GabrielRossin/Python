import math
num1 = int(input('Enter for number: '))

unidade = num1 % 10
dezena = (num1 % 100) // 10
centena = (num1 % 1000) // 100
milhar = (num1 % 10000) // 1000

print('Unidade:{}'.format(unidade))
print('Dezena:{}'.format(dezena))
print('Centena:{}'.format(centena))
print('Milhar:{}'.format(milhar))



