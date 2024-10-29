l=list
a= b = 1
n = int(input("введите диапазон"))
print(a, b)
for i in range(2, n):
   a, b = b, a + b
   print( b)