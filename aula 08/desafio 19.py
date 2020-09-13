import random
n1 = input('Enter the name of the student 1')
n2 = input('Enter the name of the student 2')
n3 = input('Enter the name of the student 3')
n4 = input('Enter the name of the student 4')
list = [n1, n2, n3, n4]
selected = random.choice(list)
print('The student selected was {}'.format(selected))