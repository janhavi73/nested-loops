word=(input("please enter your word"))
char=(input("please enter your chracter"))

i=0
count=0
while i < len(word):

    if (word[i]==char):
        count=count+1
    i=i+1

print("the number of times",char,"is repeated is",count)        
