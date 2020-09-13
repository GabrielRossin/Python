name = input('Enter the name: ')
print(name.upper())
print(name.lower())
tam = len(name.strip())
n1 = len(name.split())
n1 = n1 - 1
print(tam - n1)
first = name.split()
print(len(first[0]))

