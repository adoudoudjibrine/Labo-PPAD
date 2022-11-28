import random 
c = random.randint(1,100) # Variable choisi par le pc
print('J\'ai pense a un nombre entre 1 et 100')
n = int(input('Est ce que ton nombre est plus petit, plus grand ou egal : '))
for i in range(1,100,1):
    if c < n :
        print(f'Plus petit !')
        n = int(input('Est ce que ton nombre est plus petit, plus grand ou egal : '))
    elif c > n :
        print(f'Plus grand !')
        n = int(input('Est ce que ton nombre est plus petit, plus grand ou egal : '))
    else :
        print(f'{n} c\'est genial, le nombre auquel j\'avais pense. Bravo')
        break
    
    
    