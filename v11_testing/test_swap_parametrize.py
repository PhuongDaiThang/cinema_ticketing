# test_swap_parametrized.py
import pytest
from swap import swap_values

@pytest.mark.parametrize("input_a, input_b, expected_a, expected_b", [
	(1, 2, 2, 1),       # Test with integers
	('a', 'b', 'b', 'a'), # Test with strings
	(True, False, False, True), # Test with boolean values
])
def test_swap_values(input_a, input_b, expected_a, expected_b):
    result_a, result_b = swap_values(input_a, input_b)
    assert result_a == expected_a and result_b == expected_b