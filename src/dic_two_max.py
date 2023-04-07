"Создать программу, выводящую ключи двух максимальных элементов в словаре"


def get_max(src: dict) -> tuple:

    if not src:
        return None

    first_max = None
    second_max = None

    for key, value in src.items():

        if first_max is None or value > src[first_max]:
            second_max = first_max
            first_max = key
            continue

        if second_max is None or value > src[second_max]:
            second_max = key

    return (first_max, second_max)


def test_1():
    test_dict = {"1": 3, "2": 2, "3": 4, "5": 0}
    maxs = get_max(test_dict)
    assert maxs == ("3", "1")


def test_2():
    test_dict = {}
    assert get_max(test_dict) is None


def test_3():
    test_dict = {"1": 0, "2": 0}
    assert get_max(test_dict) == ("1", "2")


if __name__ == "__main__":
    test_1()
    test_2()
