import time
from datetime import datetime
from functools import wraps, partial
from typing import Dict

run_dict: Dict[str, int] = {}


def repeat(times):
    def decorate(func):
        print(f"Inside repeat func for {func.__name__}")

        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorate


def time_measure(func):
    print(f"Inside time measurue for func {func.__name__}")

    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = datetime.now()
        # print(f"Inside time measure wrapper. func={func.__name__}")
        func(*args, **kwargs)
        duration = (datetime.now()-start_time).total_seconds()
        print(f"Duration = {duration}")
    return wrapper


def run_calc(func):
    # run_dict: dict[str, int] = {}
    # - moved to global for store or statistic in one place
    print(f"Inside run calc for func {func.__name__}")

    @wraps(func)
    def wrapper(*args, ** kwargs):
        key = func.__name__
        if key in run_dict:
            run_dict[key] = run_dict[key]+1
        else:
            run_dict[key] = 1
        func(*args, ** kwargs)
        print(f'Function {func.__name__} is started {run_dict[key]} times')
        print(run_dict)

    return wrapper


@run_calc
def some_function_1(a: int = 0):
    print(f'Inside some function_1. a={a}')
    time.sleep(0.2)


@run_calc
@time_measure
def some_function_2(b: int = 0):
    print(f'Inside some function_2. b={b}')
    time.sleep(0.3)


@repeat(5)
@run_calc
@time_measure
def some_function_3(c: int = 0):
    print(f'Inside some function_3. c={c}')
    time.sleep(0.3)


def some_function_4(d: int = 0):
    print(f'Inside some function_4. d={d}')
    time.sleep(0.3)


if __name__ == "__main__":
    # some_function_1(1)
    # some_function_2(2)
    some_function_3(1)

    # repeat(3)(
    #     run_calc(time_measure(some_function_4))
    # )(3)
