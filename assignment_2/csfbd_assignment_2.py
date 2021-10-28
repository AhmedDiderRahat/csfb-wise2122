
# coding: utf-8

# ### Assignment: 2 

# <b> Coded By: </b> Ahmed Dider Rahat <br>
# <b> Matriculation Number: </b> 916146

# In[1]:


numbers = [ 1, 4, 6, 67, 6, 8, 23, 8, 34, 49, 67, 6, 8, 23, 37, 67, 6, 34, 19, 67, 6, 8 ]


# In[2]:


#question 1: a. Print the first four numbers (use slicing).

print("First Four numbers are: " + str(numbers[:4]))


# In[3]:


#question 1: b. Print the last four numbers.

print("Last Four numbers are: " + str(numbers[-4:]))


# In[4]:


#question 1: c. Write a Python function: sum_all( _numbers: [] ) ‐> int that computes the sum of all numbers.

def sum_all(_numbers: []):
    _sum = 0
    
    for number in _numbers:
        _sum += number
    
    return _sum
print("sum_all(numbers) -> " + str( sum_all( numbers ) ) )


# In[5]:


#question 1: d. Write a Python function: sum_odds( … ) that computes the sum of all odd numbers. 


def sum_odds(_numbers: []):
    _sum = 0
    
    for number in _numbers:
        if number % 2 == 1:
            _sum += number
    
    return _sum

print("sum_odds(numbers) -> " + str(sum_odds(numbers))) 


# In[6]:


"""question 1: e. Write a Python function: sum_four( … ) that computes the sum of the first four numbers and the 
sum of the last four numbers. Use Python’s tuple‐notation to return both values."""

def sum_four(_numbers: []):
    
    first_four = sum_all(_numbers[:4])
    last_four = sum_all(_numbers[-4:])
    
    
    return (first_four, last_four)

print("sum_four(numbers) -> " + str(sum_four(numbers)))


# In[7]:


"""question 1: f. Write a lambda function:(sum_lambda = lambda…) that computes the sum of all numbers."""

def sum_of_last_two(_numbers: []):
    first_num = _numbers[0]
    second_num = _numbers[1]
    
    _numbers.pop(0)
    
    _numbers[0] = first_num + second_num
    
    return _numbers

_numbers = numbers.copy()

sum_lambda = lambda _numbers: sum_lambda(sum_of_last_two(_numbers)) if (len(_numbers) > 1) else _numbers[0]

print("sum_lambda(numbers) -> " + str(sum_lambda(_numbers))) 


# In[8]:


"""question 1: g. Write a lambda function: sum_lambda_odds( … ) that computes the sum of all odd numbers."""

sum_lambda_odds = lambda _data: sum_lambda([i for i in _data if i%2==1])

_numbers = numbers.copy()

print("sum_lambda_odds(numbers) -> " + str(sum_lambda_odds(_numbers)))


# <b>question 1: h. Given the list contains n numbers, how many steps are needed to compute the sum of all numbers?</b>
# 
# <b>Answer:</b> If the number, n is even than it need n/2 step to compute the sum. 
# The process is: add number[0] with number[n-1], number[1] with number[n-2], and so on.
# 
# if the number, n is odd. Then need one extra itteration to add the middle element. 
# 
# So, the overall step is ceil(n/2). 

# In[9]:


"""2.) Write a Python function: find_first(_n: int, _numbers: []) -> int: that finds the first index of a number n in numbers
(or ‐1 if element is not found)."""

def find_first(_n: int, _numbers: []):
    index = 0
    
    for _num in _numbers:
        if _num==_n:
            return index
        index += 1
        
    return -1


"""Write a Python function: find_last(_n: int, _numbers: []) -> int:that finds the last index of an element in numbers
(or ‐1). """

def find_last(_n: int, _numbers: []):
    index = 0
    
    lastIndex=-1
    
    for _num in _numbers:
        if _num==_n:
            lastIndex = index

        index += 1
        
    return lastIndex

print("find_first(6,numbers) -> " + str( find_first(6,numbers)))
print("find_last(6,numbers) -> " + str( find_last(6,numbers)))


# In[10]:


"""3.) Write a Python function: find_firsttwo(_n: int, _m: int, _numbers: []) -> int: that finds the first index of two given
consecutive numbers in the list (or ‐1 if not found)."""

def find_firsttwo(_n1: int, _n2: int, _numbers: []):
    
    intentInd = -1
    
    for index in range(0, len(_numbers)-1):
        if _n1 == _numbers[index] and _n2 == _numbers[index+1]:
            intentInd = index
            break;
    
    return intentInd

print("find_firsttwo(6,8,numbers) -> " + str(find_firsttwo(6,8,numbers)))


# In[11]:


"""4.) Write a Python function: find_alltwo(_n: int, _m: int, _numbers: []) -> []:that finds all indices of the two given 
consecutive numbers appearing in the list (or empty set)."""

def find_alltwo(_n1: int, _n2: int, _numbers: []):
    
    consicutive_list = []
    
    for index in range(0, len(_numbers)-1):
        if _n1 == _numbers[index] and _n2 == _numbers[index+1]:
            consicutive_list.append(index)
            
    return consicutive_list

print("find_alltwo(67,6,numbers) -> " + str( find_alltwo(67,6,numbers) ) )


# In[12]:


"""5.) Write a Python function: find_sub(_sub: [], _numbers: []) -> int:that finds the index of the first appearance of
the sublist in the list (or ‐1)."""

def find_sub(_sub: [], _numbers: []):
    
    intentIndex = -1
    
    for index in range(0, len(_numbers)-1):
        if _numbers[index] == _sub[0]:
            _subList = _numbers[index:(index+len(_sub))]
            
            if _subList == _sub:
                return index
            
    return intentIndex

print("find_sub([67,6,8],numbers) -> " + str( find_sub([67,6,8],numbers)))


# In[13]:


"""6.) Write a Python function: find_allsubs(_sub: [], _numbers: []) -> []: that finds all occurrences of a given 
sublist in numbers (or empty set)."""

def find_allsubs(_sub: [], _numbers: []):
    
    intentIndexList = []
    
    for index in range(0, len(_numbers)-1):
        if _numbers[index] == _sub[0]:
            _subList = _numbers[index:(index+len(_sub))]
            
            if _subList == _sub:
                intentIndexList.append(index)
            
    return intentIndexList

print("find_allsubs([67,6,8],numbers) -> " + str( find_allsubs([67,6,8],numbers) ) )


# <b>7.) If numbers has n elements and the sublist has m elements, how many steps are needed to finds all occurrences of a sublist in the list?</b>
# 
# <b>Answer:</b> It needs (n - m - 1) * m steps to compute it. 
