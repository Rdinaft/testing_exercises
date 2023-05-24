from functions.level_1_5.two_square_equation import solve_square_equation


def test__solve_square_equation__discriminant_below_zero():
    assert solve_square_equation(9.3, -6.4, 2.1) == (None, None)

def test__solve_square_equation__if_discriminant_equals_zero():
    assert solve_square_equation(16, -8, 1) == (0.25, 0.25)
    assert solve_square_equation(2, 0, 0) == (0, 0)

def test__solve_square_equation__if_discriminant_above_zero():
    assert solve_square_equation(2, 5, 2) == (-2, -0.5)

def test__solve_square_equation__without_square_coefficient():
    assert solve_square_equation(0, 3, -5) == (1.6666666666666667, None)

def test__solve_square_equation__if_no_square_and_linear_coefficient():
    assert solve_square_equation(0, 0, -5) == (None, None)

def test__solve_square_equation__if_no_any_coefficient():
    assert solve_square_equation(0, 0, 0) == (None, None)
