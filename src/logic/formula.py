class SingletonMetaclass(type):

    def __init__(cls, name, bases, attrs, **kwargs):
        super().__init__(name, bases, attrs)
        cls._cache = dict()

    def __call__(cls, *args, **kwargs):
        name = args[0]
        if name in cls._cache:
            return cls._cache[name]
        cls._cache[name] = super().__call__(*args, **kwargs)
        return cls._cache[name]


class AP(metaclass=SingletonMetaclass):

    def __init__(self, name):
        self.name = name

class A:

    def __init__(self, a):
        pass


if __name__ == "__main__":
    a = AP("a")
    b = AP("a")
    print(a, id(a))
    print(b, id(b))