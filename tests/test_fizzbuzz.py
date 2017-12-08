import pytest

from fizzbuzz import fizzbuzz

number_to_expected_string = {
    1: '1',
    2: '2',
}
@pytest.mark.parametrize('number, expected_string', number_to_expected_string.items())
def test_known_number_returns_expected(number, expected_string):
    assert expected_string == fizzbuzz(number) 

# bad_values_to_expected_error = {
#     -1: ValueError,
#     0: ValueError,
#     1: ValueError,
#     'hello': ValueError,
# }
# @pytest.mark.parametrize('bad_value, expected_error', bad_values_to_expected_error.items())
# def test_known_value_returns_expected_error(bad_value, expected_error):
#     # Rendundant tests show alternate syntax.
# 
#     with pytest.raises(expected_error):
#         largest_factor(bad_value)
# 
#     # older syntax works with 2.4
#     pytest.raises(expected_error, "largest_factor(bad_value)")
