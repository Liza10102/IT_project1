def f(n, b):
   summ = 0
   n = n[::-1]
   for i in range(len(n)):
       summ += int(n[i]) * b ** i
   return summ
print(f('1000',2))
print("Hello world!")
print("Hello world!2")