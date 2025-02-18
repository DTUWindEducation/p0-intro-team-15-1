#Exercise 1

def greet(names):
    for name in names:
        print("Hello " + name)

#Exercise 2
def goldilocks(length):
    if length < 140:
        print("The bed is too small.")
    elif length > 150:
        print("The bed is too big.")
    else:
        print("The bed has a perfect size")

#Exercise 3
def square_list(numbers):
    return [x**2 for x in numbers]

#Exercise 4
def fibonacci_stop(n):
    fib_sequence = [0, 1]
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
    return cleaned_anglesgot

pitch_angles = [10, 95, 45, -5, 85]
status_signals = [0, 1, 0, 2, 0]

