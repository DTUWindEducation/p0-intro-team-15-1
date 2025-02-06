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
    i = np.argwhere(np.array(status)>0)
    x[i] = -999
    return x
    

x = [-1, 2, 6, 95]
status = [1, 0, 0, 0]

print(corr_pitch(x, status))

