def make_division_by(n: int):
    def divider_num(x: int):
        return x/n
    return divider_num

def run():
    division_by_3 = make_division_by(3)
    print(division_by_3(10))
    division_by_3 = make_division_by(5)
    print(division_by_3(100))
    division_by_3 = make_division_by(18)
    print(division_by_3(58))
if __name__ == '__main__':
    run()
