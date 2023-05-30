from functions.level_1_5.two_square_equation import solve_square_equation
import pytest


@pytest.mark.parametrize(
    "square_coefficient, linear_coefficient, const_coefficient, expected_result",
    [
        (9.3, -6.4, 2.1, (None, None)),
        (16, -8, 1, (0.25, 0.25)),
        (2, 0, 0, (0, 0)),
        (2, 5, 2, (-2, -0.5)),
        (0, 3, -5, (1.6666666666666667, None)),
        (0, 0, -5, (None, None)),
        (0, 0, 0, (None, None)),
    ],
    ids=[
        "discriminant_below_zero",
        "discriminant_equals_zero",
        "discriminant_equals_zero_with_only_square_coefficient",
        "discriminant_above_zero",
        "without_square_coefficient",
        "no_square_and_linear_coefficient",
        "no_any_coefficient",
    ],
)
def test__solve_square_equation__(
    square_coefficient, linear_coefficient, const_coefficient, expected_result
):
    assert (
        solve_square_equation(square_coefficient, linear_coefficient, const_coefficient)
        == expected_result
    )
