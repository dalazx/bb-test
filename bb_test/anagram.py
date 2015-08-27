import itertools


def find_anagrams(word, words):
    # getting all permutations of the word
    # intersecting them with the supplied words
    return set(
        ''.join(perm) for perm in itertools.permutations(word)
    ).intersection(words)
