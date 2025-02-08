<<<<<<< HEAD
#%% Exercise 1
def greet (who):
    print(f"*Silently walks past {who}*")

#%% Exercise 2

def bed(l):
    if l<140:
        print("Too small")
    elif l>150:
        print("Too big")
    else:
        print("Yes daddy")

#%% Exercise 3
import numpy as np

def square_list (l):
    return np.array(l)**2

#%% Exercise 4

def fibonacci_stop(m):
    x0=0
    x1=1
    lst=[x1]
    while x1<m:
        lst.append(x0+x1)
        x0=x1
        x1=lst[-1]
    return lst

# print(fibonacci_stop(30))

#%% Exercise 5

def corr_pitch(x, status):
    x = np.asarray(x)
    i = np.argwhere((np.array(status)>0) and (x<0 or x>90))
    x[i] = -999
    return x
    

x = [-1, 2, 6, 95]
status = [1, 0, 0, 0]

print(corr_pitch(x, status))
=======
# 1. Write Simple Function
def greet(a):
    print(f"Hello,{a}!")

# 2. If/else statments
def goldilocks(x):
    if x < 140:
        print('Too Small!')
    elif x > 150:
        print('Too Large!')
    else:
        print('Just Right!')

# 3. For Loops
def square_list(list):
    for i in list:
        print(f"[{i*i},]")

# 4 While Loops
def fibonacci_stop(x):
    fib_sequence = [1,1]
    while True:
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        if next_fib > x:
            break
        fib_sequence.append(next_fib)
    return fib_sequence

# 5 Logical Operators
def clean_pitch(x, status):
    cleaned_pitch = []
    for x, status in zip(x, status):
        if (x < 0 or x > 90) and status > 0:
            cleaned_pitch.append(-999)
        else:
            cleaned_pitch.append(x)
    return cleaned_pitch

>>>>>>> main

