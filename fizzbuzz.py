def fizzbuzz(number):
    try:
        polished_number = int(number.real)
    except (TypeError, AttributeError):
        raise ValueError
    if polished_number != number:
        raise ValueError
    number = polished_number
    terms = '' 
    if number % 3 == 0:
        terms += 'fizz'
    if number % 5 == 0:
        terms += 'buzz'
    if not terms:
        terms += str(number)
    return terms
