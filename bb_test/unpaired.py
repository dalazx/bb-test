import operator


def find_unpaired_number_reduce(numbers):
    return reduce(operator.xor, numbers)


def find_unpaired_number_forloop(numbers):
    unpaired = 0
    for number in numbers:
        unpaired ^= number
    return unpaired


find_unpaired_number = find_unpaired_number_forloop


def main():
    import timeit

    print timeit.timeit(
        'find_unpaired_number_reduce('
        'itertools.chain(xrange(9999), xrange(10000)))',
        'import itertools; from __main__ import find_unpaired_number_reduce',
        number=100000)

    print timeit.timeit(
        'find_unpaired_number_forloop('
        'itertools.chain(xrange(9999), xrange(10000)))',
        'import itertools; from __main__ import find_unpaired_number_forloop',
        number=100000)


if __name__ == '__main__':
    main()
