def sreeja(a):
    if a==1:
        return
    i=2
    while(a%i !=0):
        i=i+1
    print(i,end=" ")
    sreeja(a/i)

a=int(input("Enter the number: "))
sreeja(a)
