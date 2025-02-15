"""Test your functions from Week 2 assignment.
"""
import preclass_assignment.week00_prep_answers as fxn
import numpy as np


def test_greet(capsys):
    """Check that the greet function prints as expected"""
    # given
    name = 'world'  # who should we greet?
    # when
    fxn.greet(name)  # greet them
    captured = capsys.readouterr()  # capture what would have been printed to screen
    # then
    assert captured.out == 'Hello, world!\n'  # check that the greeting was what we expect



def test_goldilocks(capsys):
    """Check goldilocks returns expected output"""
    # given
    # when
    # then
    assert False  # TODO! Update the contents of this function so it correctly tests goldilocks


def test_square_list():
    """Check square_list returns expected output"""
    # given
    inp = [1, 2, 3]  # test input to function
    exp_out = [1, 4, 9]  # expected output
    # when
    out = fxn.square_list(inp)  # actual output
    # then
    assert exp_out == out  # throw error if actual and expected output don't match


def test_fibonacci_stop():
    """Check fibonacci functions works as expected."""
    # given
    x = np.arange(2,30)
    y_total = np.array([1,1,2,3,5,8,13,21])
    # when
    y_func = []
    for x_i in x:
        y_func.append(fxn.fibonacci_stop(x_i))
    # then
    for i, x_i in enumerate(x):
        assert isinstance(y_func[i], list), f"Output for input {x_i} is not a list"
        assert np.array_equal(y_func[i], y_total[y_total<=x_i]), f"Wrong result for input "\
            + f"{x_i}: {y_func[i]}"
        assert all(isinstance(y_i, int) for y_i in y_func[i]), "Not all "\
            + "numbers are integers"

def test_clean_pitch():
    """Check clean_pitch works as expected for a range of random angles"""
    # given
    test_length = 1000
    count_invalid_status = 100

    angles = np.random.randn(test_length)*120-15 #Create angles in range -15 to 105°
    status = np.zeros(test_length)
    i_invalid = np.random.choice(test_length, count_invalid_status,
                                 replace=False)
    status[i_invalid] = np.random.randn(count_invalid_status)*10


    i_tbc = np.argwhere((status>0) & ((angles<0) | (angles>90)))
    corr_angles = angles
    corr_angles[i_tbc] = -999
    # when
    corr_angles_func = fxn.clean_pitch(x=angles, status=status)
    # then
    assert np.array_equal(corr_angles, corr_angles_func), "Wrong results"