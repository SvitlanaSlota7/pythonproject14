class StopWords:
    def __init__(self, words: list):
        """список стоп-слів"""
        self.words = words

    def __call__(self, func):

        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)

            if isinstance(result, str):
                for word in self.words:
                    result = result.replace(word, "*")

            return result

        return wrapper

@StopWords(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


output = create_slogan("Steve")
print(f"Результат: {output}")

assert output == "Steve drinks * in his brand new *!"