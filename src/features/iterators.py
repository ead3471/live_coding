class FibonachiIterator():
    def __init__(self, max_value) -> None:
        self.value_0 = 0
        self.value_1 = 1
        self.current_element_number = 0
        self.max_value = max_value

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_element_number < self.max_value:
            result = self.value_0
            self.value_0 = self.value_1+self.value_0
            self.value_1 = result
            self.current_element_number += 1
            return result
        raise StopIteration()


def fibonachi_generator(max_number):
    current_value = 1
    sum = 0
    while max_number > 0:
        yield sum
        tmp = sum
        sum += current_value
        current_value = tmp
        max_number -= 1


def generator_with_send():
    value = 0
    while True:
        send_val = yield value
        value += 1
        print(f'send value inside ={str(send_val)} value = {value}')


def test_generator_with_send():
    gen = generator_with_send()

    print(next(gen))
    print(gen.send(5))
    print(gen.send("22"))
    print(next(gen))


def test_iterator():
    for value in FibonachiIterator(10):
        print(value, end=" ")

    result = " ".join(map(str, FibonachiIterator(10)))
    print(result)

    result_squared = [value**2 for value in FibonachiIterator(10)]

    print(" ".join(map(str, result_squared)))


def test_generator_1():
    numbers = [0, 1, 2]
    squared_gen = (value**2 for value in numbers)
    print(type(squared_gen))
    print(f'1:{list(squared_gen)}')
    print(f'2:{list(squared_gen)}')

    squared_list = [value**2 for value in numbers]
    print(type(squared_list))
    print(f'1:{list(squared_list)}')
    print(f'2:{list(squared_list)}')

    rng = range(5)
    print(type(rng))
    print(f'1:{list(rng)}')
    print(f'2:{list(rng)}')


def test_generator():
    gen = fibonachi_generator(3)
    values = [value for value in gen]
    print(values)
    values = [value for value in gen]
    print(values)


if __name__ == "__main__":
    # test_generator_1()
    test_generator_with_send()
