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


#Python Program to print Prime Number in a given range.    
def prime_print(n,m):
    nonp_lst=[]
    p_list=[]
    for i in range(n,m):
        for x in range(2,i):
            if i%x==0:
                nonp_lst.append(i)
        if i not in nonp_lst:
            p_list.append(i)
    return p_list

#Python Program to convert Celsius to Fahrenheit.
#multiply by 1.8 (or 9/5) and add 32

def find_fahren(c):
    f=(1.8*c)+32
    return f

#Python program to calculate Simple Interest with explanation.
# S.I. = P × R × T

def find_simple_interest(p,r,t):
    S=(p*r*t)/100
    return S

#Python Program to count occurrence of a given characters in string
def find_most_occurring_word(s):
    d={}
    l=s.split()
    new_list=[]
    for i in l:
        if i.isupper():
            new_list.append(i.lower())
        else:
            new_list.append(i)
    for e in new_list:
        d[e]=d.get(e,0)+1
        max_key, max_value = max(d.items(), key=lambda x: x[1])
    if max_value==1:
        print("No word occurs more than once")
    else:
        for k in d.keys():
            if d[k]==max_value:
                print(f" The Most occuring word is: {k}, and it occurs {d[k]} times")

#Python Program to check if two Strings are Anagram. cinema=iceman
#It is a word, phrase, or name formed by rearranging the letters of another
def anagram_check(a,b):
    new_list=[]
    count=0
    if len(a)==len(b):
        for x in range(len(b)):
            if b[x] in a:
                count+=1
        if len(b)==count:
            return True
        else:
            return False
    else:
        return False
    

#Python program to remove repeated character from string.

def remove_repeated(s):
    l=[]
    for i in s:
        if i not in l:
            l.append(i)
    return ''.join(l)


#Python program to calculate sum of integers in string

def calc_sum(f):
    l=[]
    summ=0
    for i in f:
        if i.isdigit():
            l.append(int(i))
            print(l)
    for x in l:
        summ+=x
    return summ


#Python program to perform left rotation of array elements by two positions

def left_rotation(t):
    new_list = []
    count = -2
    for i in range(len(t)):
        new_list.append(0)

    for i in range(len(t)):
        new_list[count] = t[i]
        count += 1
    return new_list


#Problem:

""" Given an integer, , perform the following conditional actions:

If  is odd, print Weird
If  is even and in the inclusive range of 2 to 5, print Not Weird
If  is even and in the inclusive range of 6 to 20 , print Weird
If  is even and greater than 20, print Not Weird"""

n=int(input("Input an integer"))

if n%2!=0:
    print("Wierd")
elif n%2==0 and n in range(2,5):
    print("Not Wierd")
elif n%2==0 and n in range(6,20):
    print("Wierd")
else:
    if n>20 and n%2==0:
        print("Not Wierd")



#You are given a two lists A and B. Your task is to compute their cartesian product X.
from itertools import product
a_list=input("Input a list of numbers")
a_list=a_list.split()
A=[]
B=[]
for i in a_list:
    A.append(int(i))
    print(A)
b_list=input("Input a list of numbers")
b_list=b_list.split()
for x in b_list:
    B.append(int(x))
    print(B)
    
new=list(product(A,B))

for y in new:
    print(y, end=' ')




#itertools.permutations(iterable[, r])
#This tool returns successive k length permutations of elements in an iterable.
#Your task is to print all possible permutations of size k of the string (S) in lexicographic sorted order.

from itertools import permutations
S=input()
S=S.split()
perm_list=S[0]
perm_list=sorted(perm_list)
k=int(S[1])


permed=list(permutations(perm_list,k))
permed=list(permed)
finale=[]

for i in permed:
    print("".join(list(i)))


#You are given a string S.
#Your task is to print all possible combinations, up to size k, of the string S in lexicographic sorted order.

from itertools import combinations
S=input()
S=S.split()
comb_list=S[0]
comb_list=sorted(comb_list)
k=int(S[1])
for x in range(1,k+1):
    for i in combinations(comb_list,x):
        print("".join(i))


#Task. You are given a string S.
#Your task is to print all possible size k replacement combinations of the string in lexicographic sorted order.
#Input Format: A single line containing the string S and integer value k separated by a space.


from itertools import combinations_with_replacement
S=input()
S=S.split()
co_list=S[0]
co_list=sorted(co_list)
k=int(S[1])
cor=list(combinations_with_replacement(co_list,k))
for i in cor:
    print("".join(list(i)))


#In this task, we would like for you to appreciate the usefulness of the groupby() function of itertools 
#You are given a string S. Suppose a character 'c' occurs consecutively X times in the string.
# Replace these consecutive occurrences of the character 'c' with (X,c) in the string.
from itertools import groupby
S=input()
character_count = []
characters = []
for X, c in groupby(S):
    character_count.append(len(list(c)))
    characters.append(X)
merged_list = list(zip(character_count, characters))
for item in merged_list:
    print("({}, {})".format(item[0], item[1]), end=' ')


"""Task

Raghu is a shoe shop owner. His shop has X number of shoes.
He has a list containing the size of each shoe he has in his shop.
There are N number of customers who are willing to pay x amount of money only if they get the shoe of their desired size.

Your task is to compute how much money Raghu earned.

Input Format

The first line contains X, the number of shoes.
The second line contains the space separated list of all the shoe sizes in the shop.
The third line contains N, the number of customers.
The next N lines contain the space separated values of the shoe size desired by the customer and x, the price of the shoe.

Output Format

Print the amount of money earned by Raghu."""

from collections import Counter
X=int(input()) #number of shoes
shoe_sizes_available=input()
shoe_sizes_available=shoe_sizes_available.split()
list_of_sizes=[]
for sizes in shoe_sizes_available:
    list_of_sizes.append(int(sizes))
print(list_of_sizes)
counter_sizes=Counter(list_of_sizes) #returns how many each shoe size has in stock
N=int(input()) #the number of customers

#Dictionary for size and price
Revenue=0
for i in range(N):
    shoe_size_and_price= input()
    size = int(shoe_size_and_price.split()[0])
    price = int(shoe_size_and_price.split()[1])
    
    if size in counter_sizes.keys():
        if counter_sizes.get(size)>0:
            counter_sizes[size]=counter_sizes.get(size)-1
            Revenue=Revenue+price
            
print(Revenue)


"""In this challenge, you will be given 2 integers, n and m. There are m words, which might repeat, in word group A. 
There are m words belonging to word group B. For each  words, check whether the word has appeared in group A or not. 
Print the indices of each occurrence of m in group A. If it does not appear, print -1.

Example

Group A contains 'a', 'b', 'a' Group B contains 'a', 'c'

For the first word in group B, 'a', it appears at positions 1 and 3 in group A. So print "1 3" next line "-1"
The second word, 'c', does not appear in group A, so print -1. """
a_and_b_size=input("A and B size")

a_and_b_size=a_and_b_size.split()
n=int(a_and_b_size[0])
m=int(a_and_b_size[1])
A=[]
B=[]

#Run a loop for n times and store values for what A will contain
for i in  range(n):
    n_words=input("n words")
    A.append(n_words)
#Run a loop for n times and store values for what B will contain
for x in range(m):
    m_words=input("m words")
    B.append(m_words)
for x in range(len(B)):
    index_remember=[]
    for y in range(len(A)):
        if B[x]==A[y]:
            index_remember.append(str(y+1))
    if index_remember==[]:
        print(-1)
    else:
        print(" ".join(index_remember))


"""Reverse a given integer. 

Example 1:
Input: x = 123
Output: 321

Example 2:
Input: x = -123
Output: -321

Example 3:
Input: x = 120
Output: 21"""


def int_reversal(integer):
    stringed_integer=str(integer)
    
    if integer<0:
        negative="-"
    else:
        negative=""
    #Postive numbers with no zeros at the end
    if integer>0 and not stringed_integer.endswith("0"):
        return stringed_integer[::-1]
    #Second Case. Negative Numbers and Numbers with Zero at the end
    if integer<0 or stringed_integer.endswith("0"):
        for i in stringed_integer:
            if stringed_integer[-1]=="0":
                stringed_integer=stringed_integer[:-1]
            if stringed_integer.startswith("-"):
                stringed_integer=stringed_integer.replace("-","")
        return(negative+stringed_integer[::-1])
    

""" Given a string s, return the longest 
palindromic substring in s.

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"""
    
    
def longest_palindrome(s):
    substrings = []
    list_of_palinds=[]
    #Run a loop to find all the substrings of s and append it to a list
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            substring = s[i:j]
            substrings.append(substring)
    #Run a loop on the created substring list and see if the reversed version of a substring is same as unrevered
    for x in substrings:
        if x==x[::-1]:
            list_of_palinds.append(x)
    longest_pal=""
    for item in list_of_palinds:
        if len(item)>len(longest_pal):
            longest_pal=item
    return longest_pal



#Optimzed code for the above coding challenge
def longest_palindrome(s):
    substrings = []
    longest_pal=""
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            substring = s[i:j]
            if substring==substring[::-1]:
                substrings.append(substring)
                if len(substring)>len(longest_pal):
                    longest_pal=substring
    return longest_pal


"""
Given a string s, find the length of the longest 
substring without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
"""

def longest_substring_length(s):
    substrings=[]
    unique_char_strings=[]
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            substring = s[i:j]
            substrings.append(substring)
    for x in substrings:
        if len(x)==len(set(x)):
            unique_char_strings.append(x)
    lengthiest_item =0
    for item in unique_char_strings:
        if len(item) >lengthiest_item:
            lengthiest_item = len(item)
    return lengthiest_item


"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
"""

def nums_and_target(nums,target):
    index_list=[]
    for i in range(len(nums)-1):
        for x in range(i+1,len(nums)):
            if nums[i]+nums[x]==target:
                index_list.append(i)
                index_list.append(x)
                #index_list+=i,x
    return index_list


"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""

def common_prefix(strs):
    shortest_item=strs[0]
    for item in strs:
        if len(item)<len(shortest_item):
            shortest_item = item
    longest_prefix=""
    
    for i in range(len(shortest_item)):
        count=0
        for x in strs:
            if x[i]!=shortest_item[i]:
                break
            count=count+1
                
        if count==len(strs):
            longest_prefix+=shortest_item[i]
        else:
            break
    return longest_prefix


"""
Find all the common characters of the given array of string
"""

def common_char(s):
    common_letters=""
    first_word=s[0]
    for i in first_word:
        count=0
        for j in s:
            if i in j:
                count+=1
        if count==len(s):
            common_letters+=i
    return common_letters


"""
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

 

Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
Example 2:

Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]
"""
def four_sum(nums,target):
    quad_list=[]
    for a in range(len(nums)-3):
        for b in range(a+1,len(nums)-2):
            for c in range(a+2,len(nums)-1):
                for d in range(a+3,len(nums)):
                    if nums[a] + nums[b] + nums[c] +nums[d] == target:
                        if a != b and a != c and a != d and b!=c and b!=d and c!=d:
                            #if the answer wants 0s not to be distinct, you can add a condition here
                            quad = nums[a], nums[b], nums[c], nums[d]
                            quad=sorted(quad)
                            if quad not in quad_list:
                                quad_list.append(quad)
    return quad_list



"""
Merge two lists together

Example 1:


Input: list1 = [1,2,4], list2 = [0,3,4]
Output: [1,1,2,3,4,4]
"""
def merging_lists(list1,list2):
    merged_list=list1+list2
    merged_list.sort()
    
    return merged_list


"""

Given an integer array nums, find the 
subarray
 with the largest sum, and return its sum.
Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
"""

def maximum_subarray(nums):
    subarrays = []
    max_list=[]
    for i in range(len(nums)):
        for j in range(i+1, len(nums)+1):
            subarray = nums[i:j]
            subarrays.append(subarray)
            if sum(subarray)>sum(max_list):
                max_list=subarray
    if len(nums)==1:
        return sum(nums)
    elif len(nums)==2:
        if nums[0]>nums[1] and nums[0]>sum(nums):
            return nums[0]
        if nums[1]>nums[0] and nums[1]>sum(nums):
            return nums[1]
        if sum(nums)>nums[0] and sum(nums)>nums[1]:
            return sum(nums)
        
    return sum(max_list)


"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""

def how_many_stairs_to_climb(n):
    ways_to_climb=0
    if n == 1:
        ways_to_climb=1
    
    if n==2:
        ways_to_climb=2
    w1=1
    w2=2
    for i in range(3, n+1):
        ways_to_climb=w1+w2
        w1=w2
        w2=ways_to_climb
    return ways_to_climb


"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
"""

def isvalid(s):
    
    strings=['(', ')', '{', '}', '[', ']']
    new_list=[]
    for i in range(len(s)):
        if s[i]==strings[0] or s[i]==strings[2] or s[i]==strings[4]:
            new_list.append(s[i])
        else:
            if len(new_list)==0:
                return False
            popped_item=new_list.pop()
            if s[i]==strings[1]:
                opening_eq=strings[0]
            elif s[i]==strings[3]:
                opening_eq=strings[2]
            elif s[i]==strings[5]:
                opening_eq=strings[4]
            if popped_item!=opening_eq:
                return False
    if len(new_list)==0:
        return True
    else:
        return False


"""
Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

The integer division should truncate toward zero, which means losing its fractional part. 
For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.

Return the quotient after dividing dividend by divisor.


Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = 3.33333.. which is truncated to 3.
Example 2:

Input: dividend = 7, divisor = -3
Output: -2
Explanation: 7/-3 = -2.33333.. which is truncated to -2.


"""

def divendisor(dividend,divisor):
    result=0
    count=0
    while result<=abs(dividend):
        result+=abs(divisor)
        count+=1
    if dividend<0 and divisor<0:
        print("first")
        return(count-1)
    elif dividend<0 or divisor<0:
        print("second")
        return (0-(count-1))
    else:
        return count-1
    
"""
Python program to insert element at a given location in Array of integers. 
Input: nums-array of integers, num1-integer,index where it should be inserted. 

"""

def insertion(nums,num1,index):
    a=index-1
    if index<=0:
        return("Please pick a number higher than 0")
    elif index<=len(nums):
        n_nums=nums[:a]+[num1]+nums[a:]
    
    else:
        return("Placement is out of range")
    print(n_nums)



#Write a program in Python to remove duplicate elements from array "s" list of nums and/or strings.
#Input:[1,2,2,4,5,4]. Output:[1,2,4,5]. Iput:["hi","hello","heya","hi","he","ih"]

def remove_duplicates(s):
    unique_list=[]
    for i in range(len(s)):
        if s[i] not in unique_list:
            unique_list.append(s[i])
    return unique_list
    

#Second solution:

def remove_duplicates(s):
    dictionary={}
    for i in s:
        if i in dictionary.keys():
            dictionary[i]+=1
        else:
            dictionary[i]=1
    for item in dictionary.keys():
        if dictionary[item]>1:
            for i in range(dictionary[item]-1):
                s.remove(item)
    return s


# Third solution

def remove_duplicates(s):
    return list(set(s))
remove_duplicates([1,2,2,2,4,5,4])



#Python program to separate characters in a given string.Input:hello. Output: "h,e,l,l,o"

def char_sep(s):
    s=",".join(s)
    print(s)

"""
Find First and Last Position of Element in Sorted Array.

Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

"""

def first_last(nums,target):
    index_list=[]
    for i in range(len(nums)):
        if nums[i]==target:
            index_list.append(i)
    
    if len(index_list)>=1:
        return [min(index_list)]+[max(index_list)]
    else:
        return [-1,-1]
    

"""
Given an array of integers nums which is sorted in ascending order, and an integer target, 
write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.
You must write an algorithm with O(log n) runtime complexity.

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1

"""


"""
first solution without binary search
def target_index(nums,target):
    for i in range(len(nums)):
        if nums[i]==target:
            return i
    if target not in nums:
        return -1
"""
#faster solution:

def index_target(nums,target):
    start=0
    end=len(nums)-1
    while start<=end:
        middle=(end+start)//2
        if nums[start]==target:
            return start
        if nums[end]==target:
            return end
        if nums[middle]==target:
            return middle
        elif end-start<=1 and nums[end]!=target and nums[start]!=target:
            return -1
        else:
            if nums[middle]<target:
                start=middle
                end=end
            else:
                start=start
                end=middle

"""
You are a product manager and currently leading a team to develop a new product. Unfortunately, 
the latest version of your product fails the quality check. 
Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one,

which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad. 

Implement a function to find the first bad version. You should minimize the number of calls to the API.


Input: n = 5, bad = 4
Output: 4
Explanation:
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
Then 4 is the first bad version.

"""
def isBadVersion(n):
    if n>=4:
        return True
    return False

def firstBadVersion(n: int) -> int:
    start=1
    end=n
    while (end-start)>4:
        middle=(end+start)//2
        if isBadVersion(middle)==True:
            start=start
            end=middle
        else:
            start=middle
            end=end

    for i in range(start,end+1):
        if isBadVersion(i)==True:
            return i
        
"""

Given a sorted array of distinct integers and a target value, return the index if the target is found. 

If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1

"""

def num_target(nums,target):
    new_list=[]
    for i in range(len(nums)):
        if nums[i]==target:
            return i
        else:
            if target not in nums:
                new_list.append(nums[i])
                new_list.append(target)
    new_list.sort()
    for x in range(len(new_list)):
        if new_list[x]==target:
            return x