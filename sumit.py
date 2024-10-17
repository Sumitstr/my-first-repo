a=[]
d=[]
c=[]
b=[]
n=int(input("Enter the number of elements in vector :"))

for i in range(0,n,1):
	c=int(input("Enter the element of vector 1 :"))
	a.append(c)
print(a)

for j in range(0,n,1):
	d=int(input("Enter the element of vector 2:"))
	b.append(d)
print(b)

r=0

for i in range(0,n,1):
	r=r+a[i]*b[i]

print(r)

print(a)
