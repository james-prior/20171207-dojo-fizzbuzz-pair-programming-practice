def fizzbuzz(input_number):
    try:
        number = int(input_number.real)
    except (TypeError, AttributeError):
        raise ValueError
    if number != input_number:
        raise ValueError

    terms = '' 
    if number % 3 == 0:
        terms += 'fizz'
    if number % 5 == 0:
        terms += 'buzz'
    if not terms:
        terms += str(number)
    return terms
