n = int(input("введите диапазон"))
l=list()
a= 0
b = 1
print(a, b, end=' ')
for i in range(2, n):
   a, b = b, a + b
   print( b, end=' ')