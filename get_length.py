#get number of digits in an int?
def get_length(num):
    n1=num%10
    num//=10

    n2=num%10
    num//=10

    n3=num%10
    num//=10

    n4=num%10
    n5=num//10
    #Get length of integer
    
    #Args:
    #    num (int): integer to get length of

    #Returns:
        #int: length of integer
    s=(n1/n1)+(n2/n2)+(n3/n3)+(n4/n4)+(n5/n5)
    return s
    # return number of digits in integer
    
x=get_length(12345)
print(x)