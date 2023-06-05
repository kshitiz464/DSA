'''def choice():
	try:
		while True:
			c=input('Do you want to Sort Arrays?(y/n) : ')
			if c in 'yY':
				a=[]
				e=1
				n=int(input('Enter the length of array:'))
				for i in range(n):
					print(i+1,'element:',end='')
					el=int(input())
					a.append(el)
				print('------MENU-----')
				print('1. Insertion Sort')
				print('2. Selection Sort')
				print('3. Bubble Sort')
				print('4. Exit')
				ch=int(input('Enter your choice!- '))
				print('Enter in which order do you want to sort? (1.Ascending or 2.Descending)',end='')
				order=int(input())
				if order==1:
					if ch==1:
						print(insertion(a))
					elif ch==2:
						print(selection(a))
					elif ch==3:
						print(bubble(a))
					else:
						print('Terminating the program! ')
						break
				elif order==2:
					if ch==1:
						rev(insertion(a))
					elif ch==2:
						rev(selection(a))
					elif ch==3:
						rev(bubble(a))
					else:
						print('Terminating the program! ')
						break
			else:
				print('Terminating Program:)')
				break
	except:
		print("Some error occured due to user's invalid input! Do you want to try again?(y/n) ",end='')
		d=input()
		if d in 'yY':
			choice()
		else:
			print('Exiting the program!')

def insertion(a):
	for i in range(1,len(a)):
		key=a[i]
		k=i-1
		while k>=0 and key<a[k]:
			a[k+1] = a[k]
			k-=1
		a[k+1]=key

	return a
def selection(a):
	for i in range(0,len(a)-1):
		min=i
		for j in range(i+1,len(a)):
			if a[j]<a[min]:
				min = j
		a[i],a[min]=a[min],a[i]		
	return a
def bubble(a):
	for i in range(0,len(a)-1):
		for j in range(i,len(a)):
			if a[i]>=a[j]:
				a[i],a[j]=a[j],a[i]

	return a
def rev(a):
	narr=[]
	size=len(a)
	for i in range(len(a)):
		narr.append(a[size-1])
		size-=1
	print(narr)

#def --():

choice()
#rev(bubble([1,5,3,0,2]))'''



a=30
b=50
c=a+b
print (c)