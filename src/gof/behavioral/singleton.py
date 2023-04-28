class UsualClass():
    pass


class SingletonNewImpl:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance:
            return cls.instance
        else:
            cls.instance = super().__new__(cls, *args, **kwargs)


def singleton_decorator(cls):
    instances = {}

    def wrapper(*args, **kwargs):
        print(instances)
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return wrapper


@singleton_decorator
class DecoratedUsualClass():
    pass


@singleton_decorator
class DecoratedAnotherUsualClass():
    pass


def test_SingletonNewImpl():
    assert not (UsualClass() is UsualClass())
    assert SingletonNewImpl() is SingletonNewImpl()


def test_singleton_decorator():
    assert DecoratedUsualClass() is DecoratedUsualClass()
    assert DecoratedAnotherUsualClass() is DecoratedAnotherUsualClass()


if __name__ == "__main__":
    # test_SingletonNewImpl()
    test_singleton_decorator()
