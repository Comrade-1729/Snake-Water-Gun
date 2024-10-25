""" 
    Calculator using Python 
"""
a=int(input(("Enter First Number : ")))
b=int(input(("Enter Second number : ")))
c=input("'add', 'subtract', 'multiply', 'divide', 'expo', "
        "'mod' or 'floor' ? \n Enter an operation : "
        )

if c=="add" :
    print("The Sum is : ", a+b)
elif c=="subtract" :
    print("The Difference is : ", a-b)
elif c=="multiply" :
    print("The Product is : ", a*b)
elif c=="divide" :
    print("The Quotient is : ", a/b)
elif c=="expo" :
    print("The Exponent is : ", a**b)
elif c=="mod" :
    print("The Remainder is : ", a%b)
elif c=="floor" :
    print("The Floor Quotient is : ", a//b)
else:
    print("Wrong Input !!!")
