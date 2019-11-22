with open('alkaline_metals.txt', 'r') as file:
    result=[]
    for line in file:
        value = line.split()
        result.append(value)
file.close()
print(result)
        
    
        
      

