for entry in range(100):
    if entry % 3 == 0 and not entry % 5 == 0:
        print('Fizz')

    elif entry % 5 == 0 and not entry % 3 == 0:
        print('Buzz')

    elif entry % 5 == 0 and entry % 3 == 0:
        print('FizzBuzz')

    else:
        print(entry)
