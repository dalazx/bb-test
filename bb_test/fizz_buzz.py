#!/usr/bin/env python


def generate_fizz_buzz(numbers):
    """For each number in numbers generate either
    'Fizz' if it's a multiple of 3 or
    'Buzz' if it's a multiple of 5 or
    'FizzBuzz' if it's both
    """

    for number in numbers:
        if number % (3 * 5) == 0:
            yield 'FizzBuzz'
        elif number % 3 == 0:
            yield 'Fizz'
        elif number % 5 == 0:
            yield 'Buzz'
        else:
            yield str(number)


def main():
    numbers = xrange(1, 100)
    for result in generate_fizz_buzz(numbers):
        print result


if __name__ == '__main__':
    main()
