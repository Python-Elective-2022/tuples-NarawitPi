"""
function skip_tuples():
    take input as tuple
    create empty tuple
    for index in range(0 to length of input, skip 1 index):
        add the index to empty tuple
    :return final tuple


"""

def skip_tuples(a):
    """

    :param a: input tuple
    :return: tuple that skip one index each
    """
    final = tuple()
    for i in range(0, len(a), 2):
        final += (a[i], )
    return final


def main():
    """
    :return: test case
    """
    print(skip_tuples(('I', 'am', 'a', 'test', 'tuple')))

if __name__ == "__main__":
    main()