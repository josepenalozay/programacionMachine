class Number:

    def __init__(self, number):
        self.number = number

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, Number):
            return self.number == other.number
        return NotImplemented

    def __ne__(self, other):
        """Overrides the default implementation
        (unnecessary in Python 3)"""
        x = self.__eq__(other)
        if x is not NotImplemented:
            return not x
        return NotImplemented

    def __hash__(self):
        """Overrides the default implementation"""
        return hash(tuple(sorted(self.__dict__.items())))


class SubNumber(Number):
    pass


n1 = Number(1)
n2 = Number(1)
n3 = SubNumber(1)
n4 = SubNumber(4)

assert n1 == n2
assert n2 == n1
assert not n1 != n2
assert not n2 != n1

assert n1 == n3
assert n3 == n1
assert not n1 != n3
assert not n3 != n1

assert not n1 == n4
assert not n4 == n1
assert n1 != n4
assert n4 != n1

assert len(set([n1, n2, n3, ])) == 1
assert len(set([n1, n2, n3, n4])) == 2