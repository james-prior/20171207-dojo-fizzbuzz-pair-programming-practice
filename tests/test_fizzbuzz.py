import pytest

from fizzbuzz import fizzbuzz

number_to_expected_string = (
    (1, '1'),
    (2, '2'),
    (3, 'fizz'),
    (3., 'fizz'),
    (3.+0j, 'fizz'),
    (6, 'fizz'),
    (5, 'buzz'),
    (10, 'buzz'),
    (15, 'fizzbuzz'),
    (30, 'fizzbuzz'),
)
@pytest.mark.parametrize('number, expected_string', number_to_expected_string)
def test_known_number_returns_expected(number, expected_string):
    # with open('log', 'a') as f:
    #     print(repr((number, expected_string)), file=f)
    #     print(len(number_to_expected_string), file=f)
    assert expected_string == fizzbuzz(number) 

bad_values_to_expected_error = {
    'hello': ValueError,
    'goodbye': ValueError,
    3.1415926: ValueError,
    2.7182818: ValueError,
    (1, 2): ValueError,
}
@pytest.mark.parametrize('bad_value, expected_error', bad_values_to_expected_error.items())
def test_known_value_returns_expected_error(bad_value, expected_error):
    # Rendundant tests show alternate syntax.

    with pytest.raises(expected_error):
        fizzbuzz(bad_value)

    # older syntax works with 2.4
    pytest.raises(expected_error, "fizzbuzz(bad_value)")
