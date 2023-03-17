#Finding Armstrong Number
def arm_num(n):
    n_lst=list(str(n))
    sum_of=0
    for i in range(len(n_lst)):
        sum_of+=(int(n_lst[i])**3)
    if sum_of==n:
        return True
    else:
        return False
    

#Palindrome Check
def palindrome(a):
    b=[]
    c=""
    for i in range(len(a)):
        if a[i]!=" " and a[i]!="?" and a[i]!="!" and a[i]!=".":
            if a[i].isupper():
                b.append(a[i].lower())
            else:
                b.append(a[i])
    c=" ".join(b)
    if c==c[::-1]:
        return True
    return False


#check if a given number is a prime
def prime_check(n):
    count=0
    for i in range(2,n):
        if n%i==0:
            count+=1
    if count>=1:
        return False
    
    else:
        return True
    


#write a program to calculate factorial
def fac_cal(n):
    mult=1
    for i in range(1,n+1):
        mult=mult*i
    return mult


#3) Write a python program which accepts a list of integers and returns the mean, median and mode of those.

def mmm_check(l):
    sl=sorted(l)
    mean=0
    meanof=0
    median=0
    mode=0
    modecount=0
    d={}
    a=len(sl)//2
    for i in sl:
        mean=(mean+i)
        d[i]=d.get(i,0)+1
        max_key, max_value = max(d.items(), key=lambda x: x[1])
    if max_value>1:
        print(f"The Mode is:{max_key} and it occurs {max_value} times")
    else:
        print(" There is No mode")
    meanof=mean/(len(sl))
    print (f" Mean of the list is: {meanof}")
    if len(sl)%2==0:
        median=(sl[a]+sl[a-1])/2
        print (f" Median of the list is: {median}")
    else:
        median=a
        print (f" Median of the list is: {median}")


#4) Write a program in Python to find greatest among a given list of integers?
def greatest(lst):
    l=sorted(lst)
    return (f"Greatest number of the list is: {l[-1]}")


#Second solution:
def greatest_num(lst):
    return max(lst)

#Third solution:
def greatest_integer(lst):
    max_num = None
    for i in range(len(lst)):
        if max_num == None:
            max_num = lst[i]
        if lst[i] > max_num:
            max_num=lst[i]
    return max_num


#5) Write a python program to check if a given number is a perfect number
#Positive integer that is equal to the sum of its proper divisors. The smallest perfect number is 6(the sum of 1, 2, and 3)
#Other perfect numbers are 28, 496, and 8,128. 
def perfect_number(n):
    divisor_list=[]
    sum_of_d=0
    for i in range(1,n):
        if n%i==0:
            divisor_list.append(i)
    for i in divisor_list:
        sum_of_d+=i
    if sum_of_d==n:
        return True
    else:
        return False
    

#Write a program in Python to swap two numbers using third variable?
#a = 1 and b = 2. Swap values of a and b. (Dont use google for this one)

def swappy(a,b,c=0):
    c=a
    a=b
    b=c
    return (f"a is: {a}, b is: {b}")