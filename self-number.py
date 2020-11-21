def getSum(n): 
  
    sum1 = 0; 
    while (n != 0): 
        sum1 = sum1 + n % 10; 
        n = n // 10; 
      
    return sum1; 
  
def isSelfNum(n): 
  
    for m in range(1, n + 1): 
        if (m + getSum(m) == n): 
            return False; 
      
    return True; 

result = 0
for i in range(1,10000) :
  if (isSelfNum(i)):
    result += i

print(result)

#result = 4897156