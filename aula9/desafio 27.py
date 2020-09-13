name = input('Enter the name:')
div_name = name.split()
cont = len(div_name) - 1
#cont = name.count(' ')
print('First name is: {}'.format(div_name[0]))
print('Last name is: {}'.format(div_name[cont]))