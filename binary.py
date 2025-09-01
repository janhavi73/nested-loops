number=int(input("please enter a number"))
if number==0:
    binary_string="0"
else:
    binary_string=" "
    original_number=number

    while number>0:
        remainder=number %2

        binary_string=str(remainder)+binary_string
        number=number //2
print(f"the decimal number {original_number} is {binary_string} in binary")        
       