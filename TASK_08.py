'''Задача 8.
	Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
	если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
	Пример:
	3 2 4 -> yes
	3 2 1 -> no'''
	

n,m,k = int(input('Введите длину шоколадки (n): ')),int(input('Введите ширину шоколадки (m): ')),int(input('Введите кол-во отламываемых долек (k): '))
if k%n == 0 or k%m == 0:
	    print('Yes')
else: print('No')



