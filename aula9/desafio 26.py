phrase = input('ENTER THE PHRASE: ')
cont_a = phrase.count('A')
pos_first = phrase.find('A')+1
pos_end = phrase.rfind('A')+1
print('The total of letters A is:{},the first position is {},the end'
      ' position is {}'.format(cont_a, pos_first, pos_end))