terms = int(input("Enter no. of terms to be print:  "))
result = list(map(lambda x: 2 ** x, range(terms)))
for i in range(terms):
   print("2 raised to power",i,"is",result[i])
