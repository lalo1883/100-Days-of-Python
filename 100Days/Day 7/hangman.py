HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

chosen_word = input('Write a word to guess: ')
word_len = len(chosen_word)
chosen_word = chosen_word.lower()


# Función para crear espacios en blanco del mismo tamaño que la palabra
def generate_blanks(word):
    blanks = []
    for i in word:
        i = '_'
        blanks.append(i)
    return blanks


word_blanks = generate_blanks(chosen_word)
print(word_blanks)


# Función para verificar si la letra está en la palabra
def char_in_word(char):
    found = False
    for i in range(word_len):
        letter = chosen_word[i]
        if letter == char:
            word_blanks[i] = letter
            found = True
    return found


def display_hangman(lives):
    print(HANGMANPICS[6 - lives])


def play():
    lives = 6
    guessed_letters = []  # Lista para almacenar letras ya adivinadas
    while lives != 0:
        guess = input('Guess a letter in the word: ')
        guess = guess.lower()

        # Verificar si la letra ya ha sido adivinada
        if guess in guessed_letters:
            print('You already used that letter. Try another letter.')
            continue

        # Agregar la letra a la lista de letras adivinadas
        guessed_letters.append(guess)

        # Verificar si la letra está en la palabra
        if char_in_word(guess):
            print(word_blanks)
            if '_' not in word_blanks:
                print('You won!')
                break
        else:
            lives -= 1
            display_hangman(lives)
            print(f'Lives: {lives}')
            if lives == 0:
                print('You lost!')


play()
