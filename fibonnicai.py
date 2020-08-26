n=int(input("Enter number of terms to be printed in series"))
a=0
b=1
print(a,b)
for i in range(n-2):
      s=a+b
      print(s)
      a=b
      b=s
      s=0
print ("this is fibonnicai series")      
