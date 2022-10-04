def calc():
    a=input('Type your first operand')
    b=input('Type your second operand')
    o=input('Type your operator')
    if o=='+':
        print(float(a)+float(b))
    elif o=='*':
        print(float(a)*float(b))
    elif o=='^':
        print(float(a)**float(b))
    elif o=='%':
        print(float(a)%float(b))
    elif o=='/':
        print(float(a)/float(b))
    else:
        print("Invalid operation.")
        
calc()   
     
