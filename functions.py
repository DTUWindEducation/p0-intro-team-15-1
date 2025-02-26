#Exercise 1

def greet(names):
<<<<<<< HEAD
    for name in names:
        print("Hello " + name)
=======
    for name in [names]:
        print("Hello, " + name + "!")
>>>>>>> 29eb1fdd48dba8731b1b956c7d5b365a122fed22

#Exercise 2
def goldilocks(length):
    if length < 140:
        print("Too Small!")
    elif length > 150:
        print("Too Big!")
    else:
        print("The bed has a perfect size")

#Exercise 3
def square_list(numbers):
    return [x**2 for x in numbers]

#Exercise 4
def fibonacci_stop(n):
    fib_sequence = [1, 1]
    while True:
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        if next_fib > n:
            break
        fib_sequence.append(next_fib)
    return fib_sequence


#Exercise 5
def clean_pitch(pitch_angles, status_signals):
    cleaned_angles = []
    for angle, status in zip(pitch_angles, status_signals):
        if (angle < 0 or angle > 90) and status > 0:
            cleaned_angles.append(-999)
        else:
            cleaned_angles.append(angle)
    return cleaned_angles

pitch_angles = [10, 95, 45, -5, 85]
status_signals = [0, 1, 0, 2, 0]

