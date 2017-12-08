def fizzbuzz(number):
    if number % 15 == 0:
        output = 'fizzbuzz'
    elif number % 5 == 0:
        output = 'buzz'
    elif number % 3 == 0:
        output = 'fizz'
    else:
        output = str(number)
    return output
