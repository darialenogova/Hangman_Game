import random

HANGMANPICS = [
    """
      +---+
      |   |
          |
          |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========
    """
]

CATEGORIES = {
    "еда": ["яблоко", "банан", "апельсин", "груша", "вишня"],
    "животные": ["слон", "тигр", "крокодил", "жираф", "панда"],
    "кухонные принадлежности": ["сковорода", "нож", "вилка", "ложка", "тарелка"],
    "транспорт": ["автомобиль", "поезд", "самолет", "велосипед", "корабль"]
}

def show_rules():
    print("""
ПРАВИЛА: У вас есть 6 попыток, чтобы угадать слово.
Повторные буквы вводить нельзя!
    """)

def choose_category():
    while True:
        theme = input("Выберите тему (еда, животные, кухонные принадлежности, транспорт): ").lower()
        if theme in CATEGORIES:
            return random.choice(CATEGORIES[theme])
        print("Неправильно указана тема. Попробуйте снова.")

def display_word(secret_word, guessed_letters):
    return "".join([letter if letter in guessed_letters else "*" for letter in secret_word])

def get_valid_letter(guessed_letters):
    while True:
        letter = input("Введите букву: ").lower()
        if len(letter) != 1 or not letter.isalpha():
            print("Ошибка: введите одну букву.")
        elif letter in guessed_letters:
            print("Вы уже вводили эту букву.")
        else:
            return letter

def process_guess(secret_word, letter, guessed_letters, attempts):
    guessed_letters.append(letter)
    if letter not in secret_word:
        attempts += 1
    return attempts

def is_word_guessed(secret_word, guessed_letters):
    for letter in secret_word:
        if letter not in guessed_letters:
            return False
    return True

def play_game(secret_word):
    guessed_letters = []
    attempts = 0
    max_attempts = len(HANGMANPICS) - 1

    while attempts < max_attempts:
        print(HANGMANPICS[attempts])
        print("Слово:", display_word(secret_word, guessed_letters))
        letter = get_valid_letter(guessed_letters)
        attempts = process_guess(secret_word, letter, guessed_letters, attempts)

        if is_word_guessed(secret_word, guessed_letters):
            print("Поздравляем! Вы угадали слово:", secret_word)
            return
    
    print(HANGMANPICS[max_attempts])
    print("Вы проиграли! Загаданное слово было:", secret_word)

def main():
    while True:
        show_rules()
        secret_word = choose_category()
        play_game(secret_word)
        if input("Хотите сыграть еще раз? (да/нет): ").lower() != "да":
            print("Спасибо за игру!")
            break

if __name__ == "__main__":
    main()
