lower=int(input("please enter the lowest range"))
upper=int(input("please enter the highest range"))



for num in range(lower, upper +1):
    if num > 1:
        for i in range(2, num):
            if (num%i)==0:
                break
        else:
            print("the prime numbers between",lower,"and",upper,"are",num)