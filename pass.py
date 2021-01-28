import random

def generator(number):
	chars = 'qwertyuiopasdfghjklzxcvbnm-=-"::{>?<?<{"L&^!(*#(*^*%!@0987654321QWERTYUIOPASDFGHJKLZXCVB>'
	chars_arr = list(chars)
	num = int(number)

	password = ''
	for x in range(0, num):
		password += chars_arr[random.randint(0,len(chars_arr))]

	print(password)

	return password
	
generator(14)
