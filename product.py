num=int(input("please enter a number"))
t=num
numlen=0
while t>0:
    numlen=numlen+1
    t=t/10

if numlen>=4:
    numlen=int(numlen/2)
    chk=0
    while num>0:
        rem=num%10
        if chk==numlen:
            midOne=rem
        elif chk==(numlen-1):
            midTwo=rem 
        num=int(num/10)                   
        chk=chk+1
    prod=midOne*midTwo
    print("\nproduct of middle digits("+str(midOne)+"*"+str(midTwo)+")=,prod")
    
else:
    print("\nit's not a 4 or more than 4 digit number!")