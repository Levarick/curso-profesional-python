def closure(num: int):
    def nested(string: str) -> str:
        return string * num
    return nested


def run():
    repeat_5 = closure(5)
    print(repeat_5("Hola"))
    repeat_10 = closure(10)
    print(repeat_10("Trabajo"))


if __name__ == '__main__':
    run()