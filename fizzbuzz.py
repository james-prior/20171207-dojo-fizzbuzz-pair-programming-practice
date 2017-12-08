def fizzbuzz(number):
    try:
        good = number == int(number.real)
    except (TypeError, AttributeError):
        raise ValueError
    if not good:
        raise ValueError
    number = int(number.real)
    terms = '' 
    if number % 3 == 0:
        terms += 'fizz'
    if number % 5 == 0:
        terms += 'buzz'
    if not terms:
        terms += str(number)
    return terms
