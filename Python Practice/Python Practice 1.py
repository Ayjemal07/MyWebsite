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