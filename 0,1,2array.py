#Q) We have only 0,1,2s in a array, and we have to sort this array.
#But the catch is to iterate it in only one loop.
a=[0,1,2,1,0,2,2,1,0,1,2]
def ar012(a):
	b=a.index(1)
	n=[]
	for i in range(len(a)):
		if a[i]==1 and l==0:
			n.append(a[i])
		elif a[i]==1 and l!=0:
			n.insert(1,a[i])
		elif a[i]<1:
			n.insert(0,a[i])
			l+=1
		else:
			n.insert(2,a[i])
			l+=1
	#n.remove(k)
	return n
print(ar012(a))



