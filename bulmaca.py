import random

def get_random_word():
    words = ["python", "java", "ruby", "javascript", "csharp", "php", "html", "css"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def is_word_guessed(word, guessed_letters):
    for letter in word:
        if letter not in guessed_letters:
            return False
    return True

def main():
    print("Bulmaca Oyununa Hoş Geldiniz!")
    word = get_random_word()
    guessed_letters = []
    attempts = 6

    while attempts > 0 and not is_word_guessed(word, guessed_letters):
        print("\nKelime:", display_word(word, guessed_letters))
        guess = input("Bir harf tahmin edin: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Geçersiz giriş! Sadece bir harf girebilirsiniz.")
            continue

        if guess in guessed_letters:
            print("Bu harfi zaten tahmin ettiniz.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Doğru tahmin!")
        else:
            attempts -= 1
            print(f"Yanlış tahmin! Kalan hakkınız: {attempts}")

    if is_word_guessed(word, guessed_letters):
        print(f"Tebrikler! Kelimeyi doğru tahmin ettiniz. Kelime: {word}")
    else:
        print(f"Maalesef, tahmin hakkınız kalmadı. Kelime: {word}")

if __name__ == "__main__":
    main()
