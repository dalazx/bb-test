import functools


def generate_key(args, kwargs):
    # sorting the items to handle cases when same kwargs come in
    # different order
    sorted_kwargs_items = tuple(sorted(kwargs.items()))
    return args + sorted_kwargs_items


def lru_cache(max_size=100):
    # TODO: consider threadsafeness
    def decorator(decorated_function):
        cache = {}
        PREV, NEXT, KEY, VALUE = 0, 1, 2, 3

        # Python 2.7 nonlocal workaround
        class Queue(object):
            __slots__ = ('root',)

            def __init__(self):
                self.root = []
                self.root[:] = [self.root, self.root, None, None]
        queue = Queue()

        @functools.wraps(decorated_function)
        def wrapper(*args, **kwargs):
            key = generate_key(args, kwargs)
            item = cache.get(key)
            if item is None:
                # miss

                value = decorated_function(*args, **kwargs)

                # TODO: nonlocal again
                cache_is_full = len(cache) == max_size
                if cache_is_full:
                    # adding the most recently used key and it's value
                    # to the queue and to the cache
                    item = queue.root
                    item[KEY] = key
                    item[VALUE] = value
                    queue.root = item[NEXT]

                    # deleting the least recently used key and it's value
                    # from the queue and from the cache
                    del cache[queue.root[KEY]]
                    queue.root[KEY] = None
                    queue.root[VALUE] = None
                else:
                    # adding a new item to the front of the queue
                    queue_front = queue.root[PREV]
                    item = [queue_front, queue.root, key, value]
                    queue_front[NEXT] = item
                    queue.root[PREV] = item

                cache[key] = item
            else:
                # hit
                # moving the most recently used key and it's value to the front
                # of the queue

                # removing the item from it's place
                item[PREV][NEXT] = item[NEXT]
                item[NEXT][PREV] = item[PREV]
                # adding the item to the front of the queue
                queue_front = queue.root[PREV]
                queue_front[NEXT] = item
                queue.root[PREV] = item
                item[PREV] = queue_front
                item[NEXT] = queue.root

                value = item[VALUE]
            return value
        return wrapper
    return decorator


@lru_cache()
def test(a):
    print a

if __name__ == '__main__':
    test('CC')
    test('DD')
