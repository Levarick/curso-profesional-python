def palindromo(word: str) -> bool:
    word = word.replace(' ', '').lower()
    return word == word[::-1]

def run():
    print(palindromo("ana"))

if __name__ == '__main__':
    run()