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


