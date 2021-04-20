def Inverted(number):
    sumn = 0
    while(number!=0 ):
        sumn=sumn*10+number%10
        number=int(number/10)
    return sumn

a=[]
x= int(input('Enter Your Number : '))
print(Inverted(x))