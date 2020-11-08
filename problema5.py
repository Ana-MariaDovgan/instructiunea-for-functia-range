i=0
n=int(input("Dati n: "))
for i in range(1,n):
    if(i%3==0) or (i%5==0):
        print(i)