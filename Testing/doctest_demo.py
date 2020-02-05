def add(a, b):
    """
    >>> add(2, 3)
    5
    >>> add(100, 200)
    300
    """
    return a + b

def double(values):
    """
    >>> double([1,2,3,4])
    [2, 4, 6, 8]

    >>> double([])
    []

    >>> double(['a', 'b', 'c'])
    ['aa', 'bb', 'cc']

    >>> double([5,6,7,8])
    [10, 12, 14, 16]
    """
    result = [value * 2 for value in values]
    print(result)