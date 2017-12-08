def fizzbuzz(number):
    terms = []
    if number % 3 == 0:
        terms.append('fizz')
    if number % 5 == 0:
        terms.append('buzz')
    if not terms:
        terms.append(str(number))
    return ''.join(terms)
