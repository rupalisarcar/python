def is_prime(num):
    if num==1:
        return False
    elif num ==2:
        return True
    else:
        for i in range(2,int((num/2)+1)):
            print(i)
            if num%i==0:
                return False
        return True        
    
result = is_prime(4)  
print(result)