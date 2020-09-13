
frase = 'Curso em Vídeo Python' #[20]

# FATIAMENTO

print(frase[9])
print(frase[9:13]) #imprime do 9 ao 12 , o 13 é excluido
print(frase[9:21:2])#imprime do 9 ao 20 , saltando de 2 em 2
print(frase[:5])#imprime do 0 ao 4
print(frase[15:])#imprime do 15 até o final
print(frase[9::3])#imprime do 9 até o final, saltando de 3 em 3
print(frase[::])#imprime toda string

# Análise
len(frase) #comprimento da frase
frase.count('o') #contar quantas vezes a letra o aparece
frase.count('0',0,13) #contar do 0 ao 12 quantas letras o aparece
frase.find('deo') #onde começa a palavra deo , se a string não existir
                 #a função retorna -1
'Curso' in frase #retorna true ou false

# Transformação

frase.replace('Python' , 'Android') #troca as palavras
frase.upper() #coloca as letras minusculas em maiusculas
frase.lower() #coloca as letras maiusculas em minusculas
frase.capitalize() #todos os caracteres vão para minusculos,exceto a primeiro letra
frase.title() #todas as iniciais das palavras vão para maiuscula

frase = '   Aprenda Python  '
frase.strip() #remove espaços inuteis
frase.rstrip() #remove somente os espaços da direita
frase.lstrip() #remove somente os espaçoes da esquerda

frase = 'Curso em Vídeo Python'

# Divisão

frase.split() #divide a string por palavra

# Junção
'-'.join(frase) #juntas as palavras com '-'
