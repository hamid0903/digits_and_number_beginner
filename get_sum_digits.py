#Find the sum of digits in an integer
def get_sum_digits(num):
    n1=num%10
    num//=10

    n2=num%10
    num//=10

    n3=num%10
    num//=10

    n4=num%10
    n5=num//10
    #Get sum of digits in integer
    
    #Args:
       # num (int): integer to get sum of digits of
    
    #Returns:
        #int: sum of digits in integer

    # return sum of digits in integer
    return n1+n2+n3+n4+n5
x=get_sum_digits(1234)
print(x)