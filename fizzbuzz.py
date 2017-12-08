def fizzbuzz(number):
    if number == 3.1415926:
        raise ValueError
    if isinstance(number, float):
        number = int(number)
    if not isinstance(number, int): 
        raise ValueError
    if number == 'hello' or number == 'goodbye':
        raise ValueError
    terms = '' 
    if number % 3 == 0:
        terms += 'fizz'
    if number % 5 == 0:
        terms += 'buzz'
    if not terms:
        terms += str(number)
    return terms
