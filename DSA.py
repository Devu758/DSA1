import math
def fac(n):
    a = 0
    for i in range (5, n+1, 5):
        a = math.floor(a+(n/i))
    return a

# GCD = HCF
# GCD(a,b)= GCD(a-b,b)
# a*b = LCM(a,b)*GCD(a,b)

def GCD(a,b):
    if a == b:
        return max(a,b)
    else:
        x = min(a,b)
        y = max(a,b)
        z= y-x
        a = z
        b = x
        return GCD(a,b)
    # for i in range (min(a,b),0,-1):
    #     if a%i == 0 and b%i == 0:
    #         return i
    # # f a <= b:
    # #     for i in range (a, 0, -1):
    # #         if a%i == 0 and b%i == 0:
    # #             return i
    # # else:
    # #     for i in range (b, 0, -1):
    # #         if a%i == 0 and b%i == 0:
    # #             return i

# def LCM(a,b):
#     x = max(a,b)
#     y = min(a,b)
#     lst = list(range(1,y+1))
#     for i in lst: 
#         if x % y == 0:
#             return x
#         else:
#             x = x*i
         
# def LCM(a, b):
#     max_num = max(a, b)
#     min_num = min(a, b)
#     lst = list(range(1, min_num+1))
#     for i in lst: 
#         if (max_num*i) % min_num == 0:
#             return max_num* i

#     return max_num 

def LCM(a,b):
    return a*b/GCD(a,b)

def prime(n):
    if n%2 ==0 and n!=2:
        return print('not prime')
    elif n%3 ==0 and n!=3:
        return print('not prime')
    else:
        for i in range(2,int(math.sqrt(n))+1,6):
            if n%i ==0 or  n%(i+2)==0:
                return print('not prime')
            else:
                return print('prime')
        
def prime_factor(n):
    for i in range(2,int(math.sqrt(n)+1)):
        while n%i ==0:
            print(i)
            n =n/i
    if n>1:
        print(n)
    
def devisor(n):
    for i in range (1,int(math.sqrt(n))+1):
        if n%i ==0:
            print(i)
    for i in range (int(math.sqrt(n))+1,0,-1):
        if n%i ==0:
            if i != n/i:
                print(int(n/i))

def seive_of_era(n):
    p = [True for i in range (0,n+1)]
    a = 2
    while a*a <=n:
        if p[a] ==True:
            for i in range (a*a,n+1,a):
                p[i]=False
        a = a+1
    print(p)
    for i in range(2,n+1):
        if p[i]:
            print(i)



        

seive_of_era(17)


# I am learning dsa