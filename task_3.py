import functools
from typing import Any


def arg_rules(type_: type, max_length: int, contains: list):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(arg: Any):
            if not isinstance(arg, type_):
                print(f"Failed: Argument must be {type_.__name__}")
                return False

            if hasattr(arg, "__len__") and len(arg) > max_length:  # type: ignore
                print(f"Failed: Argument length {len(arg)} exceeds {max_length}")
                return False

            for item in contains:
                if item not in arg:  # type: ignore
                    print(f"Failed: Argument does not contain '{item}'")
                    return False

            return func(arg)

        return wrapper

    return decorator

@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"

if __name__ == "__main__":
    print("Running Tests")

    # Має повернути False (занадто довгий)
    res1 = create_slogan('johndoe05@gmail.com')
    print(f"Result 1: {res1}")
    assert res1 is False

    # Має повернути рядок
    res2 = create_slogan('S@SH05')
    print(f"Result 2: {res2}")
    assert res2 == 'S@SH05 drinks pepsi in his brand new BMW!'

    print("All tests passed")